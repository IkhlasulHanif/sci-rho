# Dataset Generation Script Documentation

This script is designed to procedurally generate synthetic datasets for various STEM subjects (Mathematics, Physics, Chemistry, Biology, and Computer Science). It dynamically loads problem templates, generates unique problem variants using randomized seeds, and exports the data into structured JSON and Excel formats, alongside any generated images.

Here is a comprehensive guide on how to run the script and utilize its command-line flags.

## Basic Usage

To run the script with the default settings (generates 1 instance of all subjects using standard templates and a random seed), simply execute:

```bash
python generate_dataset.py
```

---

## Command-Line Flags

You can customize the generation process using the following command-line arguments:

### `--subject`
Specifies which subject(s) to generate data for.
* **Type:** String (comma-separated)
* **Default:** `all`
* **Options:** `mathematics`, `physics`, `chemistry`, `biology`, `compsci`, or `all`.
* **Example:** 
  ```
  python generate_dataset.py --subject physics,chemistry
  ```

### `--seed`
Sets the master random seed for generation. This is crucial for **reproducibility**. If you find a specific dataset generation you like or need to debug a specific output, setting the same seed will yield the exact same problems.
* **Type:** Integer
* **Default:** A random integer between 0 and 1,000,000.
* **Example:**
  ```
  python generate_dataset.py --seed 42
  ```

### `--debug`
Activates debug mode. When enabled, the script creates a `debug/` folder in the output directory and saves the text reasoning for each generated problem instance into separate `.txt` files. It also prints more verbose console logs when finding unique variants.
* **Type:** Flag (Presence activates it)
* **Default:** `False`
* **Example:**
  ```
  python generate_dataset.py --subject compsci --debug
  ```

### `--exp`
Activates experiment mode. Instead of generating a single baseline dataset, this flag forces the script to generate **10 distinct instances** (variations) of the dataset. This is highly useful for running robustness experiments or evaluations.
* **Type:** Flag (Presence activates it)
* **Default:** `False`
* **Behavior Change:** Routes output to the `experiment/sample/` directory instead of the standard `dataset/` staging folder.
* **Example:**
  ```
  python generate_dataset.py --subject mathematics --exp
  ```

### `--multi`
Activates multilingual mode. By default, the script looks for problem classes inside standard template files (e.g., `templates_001_050.py`). Activating this flag tells the script to target combined multilingual files (e.g., `<subject>_problems.py`) and specifically look for problem classes ending in `_multi`. It also dynamically injects any translated descriptions into the final JSON output.
* **Type:** Flag (Presence activates it)
* **Default:** `False`
* **Example:**
  ```
  python generate_dataset.py --subject biology --multi
  ```

### `--max_trials`
Sets the maximum number of attempts the script will make to generate a **unique** variant of a problem (verified by hashing the description and image). If it cannot find a unique variant within this limit, it logs a warning, skips the rest of that problem class, and moves on. This prevents infinite loops.
* **Type:** Integer
* **Default:** `100`
* **Example:**
  ```
  python generate_dataset.py --max_trials 500
  ```

---

## Output Structure

Depending on the flags used, the script will output files into the parent directory (`PROJECT_ROOT`) under either the `dataset/` or `experiment/` folders.

### Standard Output (No `--exp` flag)
```text
project_root/
├── dataset/
│   ├── seed.txt                  # Master seed used
│   ├── mathematics/
│   │   ├── dataset.json          # Main dataset file
│   │   ├── dataset.xlsx          # Excel version of the dataset
│   │   ├── runtime_errors.log    # Log of any classes that crashed
│   │   ├── exceeded_trials.log   # Log of classes that failed to find unique variants
│   │   ├── image/                # Generated visual assets
│   │   │   ├── image1.png
│   │   │   └── ...
│   │   └── debug/                # (If --debug is used)
│   │       ├── 1.txt
│   │       └── ...
```

### Experiment Output (`--exp` flag enabled)
```text
project_root/
├── experiment/
│   └── sample/
│       ├── mathematics_dataset.xlsx  # Multi-sheet Excel file (one sheet per instance)
│       ├── 00/                       # Instance 0
│       │   ├── seed.txt              
│       │   └── mathematics/
│       │       ├── dataset.json
│       │       └── image/
│       ├── 01/                       # Instance 1
│       │   └── ...
```