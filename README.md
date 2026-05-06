# STEM-VISION

This repository is organized into two main parts:

- Dataset generation: [dataset_generator/README.md](./dataset_generator/README.md)
- Experiments and evaluation: [experiment/README.md](./experiment/README.md)

## Repository Structure

### `dataset_generator/`
Contains the dataset creation pipeline for STEM-VISION.

See the full guide here:
[dataset_generator/README.md](./dataset_generator/README.md)

### `experiment/`
Contains experiment datasets, evaluation scripts, prompts, result folders, and analysis utilities.

See the full guide here:
[experiment/README.md](./experiment/README.md)

## Evaluation Overview

The main evaluation scripts are located in `experiment/`:

- `experiment/eval_runpod.py`
- `experiment/eval_gpt.py`
- `experiment/eval_gemini.py`
- `experiment/eval_openrouter.py`

These cover:

- local or vLLM-based evaluation
- OpenAI batch evaluation
- Gemini batch evaluation
- OpenRouter synchronous evaluation

Detailed usage, flags, and output paths are documented in:
[experiment/README.md](./experiment/README.md)

## Secrets

Provider API keys for experiment scripts live under:

```text
experiment/secrets/
```

Common key files:

- `experiment/secrets/openai_api_key.txt`
- `experiment/secrets/gemini_api_key.txt`
- `experiment/secrets/openrouter_api_key.txt`

## Where To Start

If you want to:

- generate datasets, start with [dataset_generator/README.md](./dataset_generator/README.md)
- run model evaluations, start with [experiment/README.md](./experiment/README.md)

The root README is only a short entry point. The detailed operational documentation lives in the subdirectory READMEs.
