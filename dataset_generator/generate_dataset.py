import importlib.util
import random as rnd
import argparse
import inspect
import json
import os
import sys
import re
import shutil
import time
import hashlib
import pathlib
import traceback
import pandas as pd

from biology.helper import *
from chemistry.helper import *
from compsci.helper import *
from mathematics.helper import *
from physics.helper import *

def get_file_hash(filepath: str):
    """
    Safely reads a file and returns its MD5 hash.
    Returns None if the file doesn't exist or filepath is invalid.
    """
    if not filepath or not isinstance(filepath, str) or not os.path.exists(filepath):
        return None
    
    # Read the file in chunks to avoid memory issues with large images
    hasher = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            buf = f.read(65536)
            while len(buf) > 0:
                hasher.update(buf)
                buf = f.read(65536)
        return hasher.hexdigest()
    except Exception as e:
        print(f"  [ERROR] Could not hash image {filepath}: {e}")
        return None

def get_template_classes(subject: str, multi: bool = False):
    """
    Dynamically import template classes based on the mode.
    If multi=False, loads from templates_*.py and looks for classes ending in 3 digits.
    If multi=True, loads from multi_<subject>.py and looks for classes ending in _multi.
    """
    subject_path = os.path.join(subject)
    template_classes = []
    
    # Temporarily add the subject path to sys.path so inner imports like 
    # 'from templates_001_050 import *' work correctly inside the target file.
    original_sys_path = sys.path.copy()
    sys.path.insert(0, os.path.abspath(subject_path))

    try:
        if multi:
            # MULTILINGUAL MODE: Target the combined problems file
            filename = f"multi_{subject}.py"
            filepath = os.path.join(subject_path, filename)
            
            if not os.path.exists(filepath):
                print(f"  [WARNING] Multilingual file '{filepath}' not found. Skipping subject.")
                return []
                
            module_name = f"{subject}.multi_{subject}"
            spec = importlib.util.spec_from_file_location(module_name, filepath)
            if spec is not None:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Collect classes with names ending in '_multi'
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if re.match(r".*\d{3}_multi$", name):
                        template_classes.append(obj)
        else:
            # STANDARD MODE: Loop through standard templates files
            for filename in os.listdir(subject_path):
                if filename.startswith("templates_") and filename.endswith(".py"):
                    filepath = os.path.join(subject_path, filename)
                    module_name = f"{subject}.{filename[:-3]}"  # (e.g., subject.templates_001_050)
                    
                    spec = importlib.util.spec_from_file_location(module_name, filepath)
                    if spec is None:
                        continue  # Skip bad files
                    
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    # Collect classes with last 3 characters as digits
                    for name, obj in inspect.getmembers(module, inspect.isclass):
                        if re.match(r".*\d{3}$", name):  # Ends with exactly 3 digits
                            template_classes.append(obj)
    finally:
        # Restore original path
        sys.path = original_sys_path

        # This prevents Python from reusing the previous subject's files 
        # when the next subject has files with the exact same name.
        keys_to_remove = [
            mod_name for mod_name in sys.modules 
            if mod_name.startswith("templates_")
        ]
        for key in keys_to_remove:
            del sys.modules[key]

    return template_classes

def parse_args():
    """
    Parse command-line arguments for dataset generation.
    """
    available_subjects = ["mathematics", "physics", "chemistry", "biology", "compsci"]

    parser = argparse.ArgumentParser(description="Script for dataset generation")
    parser.add_argument("--subject", type=str, default="all",
                        help=f"Subjects to include (comma-separated). Options: {available_subjects} or 'all'")
    parser.add_argument("--seed", type=int, default=rnd.randint(0,1000000),
                        help="Random seed (default: random)")
    parser.add_argument("--debug", action="store_true",
                        help="Activate debug mode (default: False)")
    parser.add_argument("--exp", action="store_true",
                        help="Generate 10 instances of dataset for experiment (default: False)")
    parser.add_argument("--multi", action="store_true",
                        help="Generate multilingual dataset using multi_<subject>.py (default: False)")
    parser.add_argument("--max_trials", type=int, default=100,
                        help="Maximum attempts to find a unique instance before skipping (default: 100)")
    
    args = parser.parse_args()

    # Handle subjects
    if args.subject == "all":
        subjects = available_subjects
    else:
        subjects = args.subject.split(",")
        # Validate subjects
        for s in subjects:
            if s not in available_subjects:
                print(f"Error: subject '{s}' is not valid. Choose from {available_subjects} or 'all'.")
                sys.exit(1)

    return subjects, args.seed, args.debug, args.exp, args.multi, args.max_trials

if __name__ == "__main__":
    start_time = time.perf_counter()

    subjects, seed, debug, exp, multi, max_trials = parse_args()

    print("Dataset generation started")
    print(f"Master Seed: {seed}")
    
    if multi:
        print("RUNNING IN MULTILINGUAL MODE (--multi)")
    if debug:
        print("RUNNING ON DEBUG MODE (--debug)")
    
    SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
    PROJECT_ROOT = SCRIPT_DIR.parent
    
    if exp:
        print("GENERATING 10 INSTANCES FOR EXPERIMENT (Subject-by-Subject mode)")
        num_of_loop = 10
    else:
        num_of_loop = 1

    for subject in subjects:
        print(f"\n=====================================")
        print(f"Generating Subject: {subject}")
        print(f"=====================================")
        
        # Reset unique history per subject
        unique_history = {}
        
        # Load existing dataset.json data to preserve old structure if needed
        # We hold num_of_loop different dataset dictionaries in memory
        datasets_data = [{} for _ in range(num_of_loop)]
        
        # Staging path where the class generator natively outputs
        staging_folder = PROJECT_ROOT / "dataset" / subject
        staging_folder.mkdir(parents=True, exist_ok=True)
        
        # Pass the multi flag to dynamically load the correct classes
        all_classes = get_template_classes(subject, multi)
        
        if not all_classes:
            continue # Skip to next subject if no classes were found
            
        count = 1
        
        # --- NEW: Lists to track both types of failures ---
        exceeded_trials_log = []
        runtime_errors_log = []
        
        for class_ in all_classes:
            class_id = class_.__name__
            unique_history[class_id] = set()
            skip_class = False  # Flag to indicate if we should abort the current class
            
            # Generate all X instances for THIS class before moving to the next class
            for index in range(num_of_loop):
                sub_seed = seed + index
                
                # Figure out where files actually need to go
                if exp:
                    target_folder = PROJECT_ROOT / "experiment" / "sample" / f"{index:02d}" / subject
                else:
                    target_folder = staging_folder
                    
                target_folder.mkdir(parents=True, exist_ok=True)
                target_img_dir = target_folder / "image"
                target_img_dir.mkdir(parents=True, exist_ok=True)

                if debug:
                    debug_folder_path = target_folder / "debug"
                    debug_folder_path.mkdir(parents=True, exist_ok=True)
                
                trials = 0
                found_unique = False
                instance = None
                
                # --- EXHAUSTIVE SEARCH LOOP ---
                while trials < max_trials:
                    attempt_seed = sub_seed + (trials * 100000)
                    rnd.seed(attempt_seed)
                    
                    try:
                        instance = class_()
                        instance.generate(count)
                    except Exception as e:
                        # Capture the full error stack trace
                        error_trace = traceback.format_exc()
                        log_msg = f"Class {class_id} (Instance {index:02d}) failed with Runtime Error:\n{error_trace}\n"
                        runtime_errors_log.append(log_msg)
                        print(f"  [RUNTIME ERROR] {class_id} crashed. Skipping entire class.")
                        skip_class = True
                        break  # Break out of the trials while loop

                    desc = getattr(instance, "description", "")
                    expected_img_path = staging_folder / "image" / f"image{count}.png"
                    img_hash = get_file_hash(str(expected_img_path))

                    signature = (desc, img_hash)

                    if signature not in unique_history[class_id]:
                        unique_history[class_id].add(signature)
                        found_unique = True
                        if trials > 0 and debug:
                            print(f"    [{class_id} - Inst {index:02d}] Unique variant found after {trials + 1} attempts.")
                        break 
                    
                    trials += 1

                # Check if we broke out due to a runtime error
                if skip_class:
                    break  # Break out of the index for-loop

                # Check if we failed to find a unique variant
                if not found_unique:
                    warning_msg = f"{class_id} (Instance {index:02d}) exceeded {max_trials} trials. Skipping entire class."
                    print(f"  [WARNING] {warning_msg}")
                    exceeded_trials_log.append(warning_msg)
                    skip_class = True
                    break  # Break out of the index for-loop

                # Process successful variant extraction
                if exp:
                    staging_img_path = staging_folder / "image" / f"image{count}.png"
                    target_img_path = target_img_dir / f"image{count}.png"
                    
                    if staging_img_path.exists():
                        shutil.copy2(staging_img_path, target_img_path)

                # Store baseline JSON data in memory
                temp_data = {
                    "description": instance.description,
                    "topic": instance.topic,
                    "subtopic": instance.subtopic,
                    "source": instance.source,
                    "curriculum": instance.curriculum,
                    "answer": instance.answer,
                    "reasoning": instance.reasoning,
                    "image": os.path.join("image", f"image{count}.png")
                }
                
                # --- NEW: Dynamically inject multilingual translations if available ---
                if multi:
                    for attr_name in dir(instance):
                        if attr_name.startswith("description_") and not attr_name.startswith("__"):
                            temp_data[attr_name] = getattr(instance, attr_name)

                datasets_data[index][f"{count}"] = temp_data

                if debug:
                    debug_file_path = debug_folder_path / f"{count}.txt"
                    with open(debug_file_path, 'w', encoding='utf-8') as file:
                        file.write(instance.reasoning)
            
            # If the class was skipped halfway, do NOT increment count and skip the completion print
            if skip_class:
                continue
            
            if exp:
                print(f"  --> Completed {num_of_loop} variants for {class_.__name__}")
                
            count += 1

        # Finished generating ALL classes for this subject. Now dump the JSONs to disk.
        for index in range(num_of_loop):
            if exp:
                target_folder = PROJECT_ROOT / "experiment" / "sample" / f"{index:02d}" / subject
                seed_path = PROJECT_ROOT / "experiment" / "sample" / f"{index:02d}" / "seed.txt"
            else:
                target_folder = staging_folder
                seed_path = PROJECT_ROOT / "dataset" / "seed.txt"

            json_path = target_folder / "dataset.json"
            
            # Write JSON
            with open(json_path, 'w', encoding="utf-8") as file:
                json.dump(datasets_data[index], file, indent=4, ensure_ascii=False)
                
            # Write Seed
            with open(seed_path, "w", encoding="utf-8") as file:
                file.write(str(seed + index))

        # --- NEW: Write all instances into a single .xlsx file ---
        if exp:
            excel_path = PROJECT_ROOT / "experiment" / "sample" / f"{subject}_dataset.xlsx"
        else:
            excel_path = staging_folder / "dataset.xlsx"
            
        try:
            with pd.ExcelWriter(excel_path) as writer:
                for index in range(num_of_loop):
                    # Convert the dictionary to a pandas DataFrame
                    df = pd.DataFrame.from_dict(datasets_data[index], orient='index')
                    df.index.name = 'No'
                    df.reset_index(inplace=True)
                    
                    # Write to a specific sheet (e.g., Instance_00, Instance_01)
                    sheet_name = f"Instance_{index:02d}"
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"  [INFO] Saved Excel dataset to {excel_path}")
        except Exception as e:
            print(f"  [ERROR] Could not save Excel file: {e}")

        # --- NEW: Write the log files if any errors were captured ---
        if exceeded_trials_log:
            exceeded_log_path = staging_folder / "exceeded_trials.log"
            with open(exceeded_log_path, "w", encoding="utf-8") as log_file:
                log_file.write(f"Classes that exceeded {max_trials} trials for {subject}:\n")
                log_file.write("-" * 50 + "\n")
                for entry in exceeded_trials_log:
                    log_file.write(f"{entry}\n")
            print(f"  [INFO] Saved log of exceeded trials to {exceeded_log_path}")

        if runtime_errors_log:
            runtime_log_path = staging_folder / "runtime_errors.log"
            with open(runtime_log_path, "w", encoding="utf-8") as log_file:
                log_file.write(f"Classes that threw runtime errors for {subject}:\n")
                log_file.write("-" * 50 + "\n")
                for entry in runtime_errors_log:
                    log_file.write(f"{entry}\n")
            print(f"  [INFO] Saved log of runtime errors to {runtime_log_path}")
                
        print(f"\n[SUCCESS] Generation loop for {subject} finished!")

    end_time = time.perf_counter()
    total_time = int(end_time - start_time)
    minutes, seconds = divmod(total_time, 60)
    print(f"\nTotal time taken: {minutes:02d}:{seconds:02d}")