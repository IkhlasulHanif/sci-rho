# Sci-ρ

Code for **Sci-Rho: A Multilingual Visually-Grounded Symbolic Benchmark for STEM Problems** ([arXiv:2606.08034](https://arxiv.org/abs/2606.08034)).

This repository contains code only. Generated benchmark instances and model outputs are not included.

This repository is organized into two main parts:

- Dataset generation: [dataset_generator/README.md](./dataset_generator/README.md)
- Experiments and evaluation: [experiment/README.md](./experiment/README.md)

## Repository Structure

### `dataset_generator/`
Contains the dataset creation pipeline for Sci-ρ.

See the full guide here:
[dataset_generator/README.md](./dataset_generator/README.md)

### `experiment/`
Contains evaluation scripts, prompts, and analysis utilities.

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

## Citation

```bibtex
@article{azmi2026scirho,
  title   = {Sci-Rho: A Multilingual Visually-Grounded Symbolic Benchmark for STEM Problems},
  author  = {Azmi, Muhammad Falensi and Hanif, Ikhlasul Akmal and Putra, Vallerie Alexandra and Yeltay, Adi and Mubarak, Abdullah and Koto, Fajri},
  journal = {arXiv preprint arXiv:2606.08034},
  year    = {2026}
}
```
