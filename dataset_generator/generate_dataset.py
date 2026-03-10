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

def get_template_classes(subject: str):
    """
    Dynamically import all <subject>/templates_*.py and return all template classes
    where the class name ends with 3 digits.
    """
    subject_path = os.path.join(subject)
    template_classes = []

    # Loop through files (e.g., templates_001_050.py)
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
    parser.add_argument("--debug", type=bool, default=False,
                        help="Activate debug mode (default: False)")
    parser.add_argument("--exp", type=bool, default=False,
                        help="Generate 10 instances of dataset for experiment (default: False)")
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

    return subjects, args.seed, args.debug, args.exp, args.max_trials

if __name__ == "__main__":
    start_time = time.perf_counter()

    subjects, seed, debug, exp, max_trials = parse_args()

    print("Dataset generation started")
    print(f"Master Seed: {seed}")
    if debug:
        print("RUNNING ON DEBUG MODE")
    
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
        
        all_classes = get_template_classes(subject)
        count = 1
        
        for class_ in all_classes:
            class_id = class_.__name__
            unique_history[class_id] = set()
            
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
                    
                    instance = class_()
                    instance.generate(count)

                    desc = getattr(instance, "description", "")
                    expected_img_path = staging_folder / "image" / f"image{count}.png"
                    img_hash = get_file_hash(str(expected_img_path))

                    signature = (desc, img_hash)

                    if signature not in unique_history[class_id]:
                        unique_history[class_id].add(signature)
                        found_unique = True
                        if trials > 0 and debug:
                            print(f"    [{class_.__name__} - Inst {index:02d}] Unique variant found after {trials + 1} attempts.")
                        break 
                    
                    trials += 1

                if not found_unique:
                    print(f"  [WARNING] Exceeded {max_trials} trials for {class_.__name__} (Instance {index:02d}).")

                # If we are running in exp mode, the generated image is sitting in the staging folder 
                # (e.g. dataset/physics/image/image1.png). We must extract it NOW before the next index overwrites it.
                if exp:
                    staging_img_path = staging_folder / "image" / f"image{count}.png"
                    target_img_path = target_img_dir / f"image{count}.png"
                    
                    if staging_img_path.exists():
                        shutil.copy2(staging_img_path, target_img_path)

                # Store JSON data in memory
                datasets_data[index][f"{count}"] = {
                    "description": instance.description,
                    "topic": instance.topic,
                    "subtopic": instance.subtopic,
                    "source": instance.source,
                    "curriculum": instance.curriculum,
                    "answer": instance.answer,
                    "reasoning": instance.reasoning,
                    "image": os.path.join("image", f"image{count}.png")
                }

                if debug:
                    debug_file_path = debug_folder_path / f"{count}.txt"
                    with open(debug_file_path, 'w', encoding='utf-8') as file:
                        file.write(instance.reasoning)
            
            # Print completion block only if running experiment
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
                json.dump(datasets_data[index], file, indent=4)
                
            # Write Seed
            with open(seed_path, "w", encoding="utf-8") as file:
                file.write(str(seed + index))
                
        print(f"\n[SUCCESS] All classes of {subject} successfully generated and deployed!")

    end_time = time.perf_counter()
    total_time = int(end_time - start_time)
    minutes, seconds = divmod(total_time, 60)
    print(f"\nTotal time taken: {minutes:02d}:{seconds:02d}")