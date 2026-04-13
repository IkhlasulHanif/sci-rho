# Experiment Documentation

## Setup and Installation

We use [uv](https://github.com/astral-sh/uv) for lightning-fast Python dependency management. Make sure you have your virtual environment created and activated (e.g., `uv venv env_name`), then start by installing the dependencies:

```bash
uv pip install -r requirements.txt
```

---

## Evaluation Pipeline

### Configuration (`config.py`)
The main evaluation script is driven by `config.py`. Before running any evaluations, you must set up your parameters there. 

The `eval_runpod.py` script automatically loads and saves its configurations from `config.py`, which includes:
* **ModelConfig:** Setup for vLLM (dtype, memory utilization, tensor parallel size, etc.).
* **SamplingConfig:** Generation parameters (temperature, max tokens).
* **ExperimentConfig:** The list of models to evaluate, the subjects to test, and the number of instances to process.

### Running `eval_runpod.py`
Once your packages are installed and your settings are finalized in `config.py`, you can run the evaluation script. 

To execute the script using `uv`, run the following command from your project root:

```bash
uv run eval_runpod.py
```
*(Note: If your script is located inside a subfolder, simply point to that path, e.g., `uv run experiment/eval_runpod.py`)*

As the script runs, it will process the datasets, query the models via vLLM, and automatically save the results as `.xlsx` files inside the `result/raw/` directory.

---

## Next Sections (Placeholder)
*(Future scripts, data generation pipelines, and tools will be documented here)*