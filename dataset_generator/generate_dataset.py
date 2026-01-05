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

from pathlib import Path
from biology.helper import *
from chemistry.helper import *
from compsci.helper import *
from mathematics.helper import *
from physics.helper import *

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

    parser = argparse.ArgumentParser(
        description="Script for dataset generation"
    )
    parser.add_argument(
        "--subject",
        type=str,
        default="all",
        help=f"Subjects to include (comma-separated). Options: {available_subjects} or 'all' (default: all)"
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=rnd.randint(0,1000000),
        help="Random seed (default: 42)"
    )
    parser.add_argument(
        "--debug",
        type=bool,
        default=False,
        help="Activate debug mode (default: False)"
    )

    parser.add_argument(
        "--exp",
        type=bool,
        default=False,
        help="Generate 10 instances of dataset for experiment (default: False)"
    )
    
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

    return subjects, args.seed, args.debug, args.exp

if __name__ == "__main__":
    start_time = time.perf_counter()

    subjects, seed, debug, exp = parse_args()

    print("Dataset generation started")
    print(f"Master Seed: {seed}")
    if debug:
        print("RUNNING ON DEBUG MODE")
    
    if exp:
        print("GENERATING 10 INSTANCES FOR EXPERIMENT")
        num_of_loop = 10
        # Path to this script ('dataset_generator/')
        SCRIPT_DIR = Path(__file__).resolve().parent

        # Project root (one level up from 'dataset_generator/')
        PROJECT_ROOT = SCRIPT_DIR.parent

        # Source: project_root/dataset
        src = PROJECT_ROOT / "dataset"
    else:
        num_of_loop = 1

    for index in range(num_of_loop):
        sub_seed = seed + index # to make seed unique for each instances when generating 10 instances of problem
        print(f"Sub Seed: {sub_seed}")
        for subject in subjects:
            print(f"Subject: {subject}\n")

            destination_folder = os.path.join(
                os.path.dirname(os.getcwd()), "dataset", subject
            )
            os.makedirs(destination_folder, exist_ok=True)
            json_path = os.path.join(destination_folder, "dataset.json")

            if os.path.exists(json_path):
                with open(json_path, "r") as file:
                    data = json.load(file)
            else:
                data = {}

            if debug:
                debug_folder_path = os.path.join(destination_folder, "debug")
                os.makedirs(debug_folder_path, exist_ok=True)

            count = 1
            all_classes = get_template_classes(subject)
            for class_ in all_classes:
                instance = class_()
                instance.generate(count)
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

                if debug:
                    debug_file_path = os.path.join(debug_folder_path, f"{count}.txt")
                    with open(debug_file_path, 'w') as file:
                        file.write(instance.reasoning)

                data[f"{count}"] = temp_data

                print(f"Generated Instance Number {count}")

                count += 1

            json_data = json.dumps(data, indent=4)
            with open(json_path, 'w') as file:
                file.write(json_data)

            print(f"All instances of {subject} are sucessfully generated!\n")

        seed_path = os.path.join(os.path.dirname(os.getcwd()), "dataset", "seed.txt")
        with open(seed_path, "w") as file:
            file.write(str(sub_seed))

        if exp:
            # destination at 'experiment/sample/01', 'experiment/sample/02', etc.
            dst = os.path.join(PROJECT_ROOT, 'experiment', 'sample', f'0{index}')

            # Copy folder and rename
            shutil.copytree(src, dst, dirs_exist_ok=True)
    
    # benchmark time
    end_time = time.perf_counter()
    total_time = int(end_time - start_time)
    minutes, seconds = divmod(total_time, 60)
    print(f"Total time taken: {minutes:02d}:{seconds:02d}")