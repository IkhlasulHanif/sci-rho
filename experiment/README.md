# Experiment Documentation

## Setup and Installation

We use [uv](https://github.com/astral-sh/uv) for Python dependency management.

Create and activate a virtual environment, then install dependencies:

```bash
uv pip install -r requirements.txt
```

## Evaluation Scripts

The main evaluation scripts in this folder are:

- `eval_runpod.py`
- `eval_gpt.py`
- `eval_gemini.py`
- `eval_openrouter.py`

All scripts expect the experiment dataset to be available under `sample/` inside `experiment/`.

## Secrets

Create an `experiment/secrets/` directory for provider API keys.

Expected files:

- `experiment/secrets/openai_api_key.txt`
- `experiment/secrets/gemini_api_key.txt`
- `experiment/secrets/openrouter_api_key.txt`

Each file should contain the API key on the first line.

Notes:

- `eval_gpt.py` falls back to environment variables if `openai_api_key.txt` is missing.
- `eval_gemini.py` falls back to environment variables if `gemini_api_key.txt` is missing.
- `eval_openrouter.py` expects `openrouter_api_key.txt` directly and exits if it is missing.

## `eval_runpod.py`

This script runs local or RunPod-style evaluation through `vLLM`.

### Configuration

`eval_runpod.py` uses `config.py` for:

- `ModelConfig`
- `SamplingConfig`
- `ExperimentConfig`

Before running, make sure `config.py` is set correctly for:

- model names
- subject list
- number of instances
- debug mode
- sampling parameters

It also requires:

- `user_prompt.txt`
- dataset files under `sample/0x/<subject>/dataset.json`

### Run

From the project root:

```bash
uv run experiment/eval_runpod.py
```

Results are saved as `.xlsx` files under:

```text
experiment/result/raw/<subject>/0x/
```

## `eval_gpt.py`

This script evaluates the dataset with OpenAI models using a staged batch workflow.

### Default Models

The script currently defines its models inside the file:

- `gpt-5.4-2026-03-05`

### Required Files

Before running, make sure these are available:

- `user_prompt.txt`
- `image_temp/image_urls.json`
- experiment data under `sample/0x/<subject>/dataset.json`

For `sample_disprop` mode, the script uses:

- `image_temp/image_urls_disprop.json`
- subjects `math_disprop` and `math_original`

API credentials are loaded from:

- `secrets/openai_api_key.txt`

If that file is not present, the script falls back to environment variables supported by the OpenAI SDK.

### Workflow

The script is stateful and split into stages:

- `--prepare`: build `.jsonl` batch request files locally
- `--send`: upload prepared requests and create OpenAI batch jobs
- `--check`: check batch job status
- `--retrieve`: download outputs and reconstruct Excel result files
- `--debug`: prepare only instance `00`
- `--retry-missing`: only regenerate missing blank responses and merge them back
- `--mode sample|sample_disprop`: choose which dataset folder to evaluate

### Typical Usage

Prepare requests:

```bash
uv run experiment/eval_gpt.py --prepare
```

Debug on instance `00` only:

```bash
uv run experiment/eval_gpt.py --prepare --debug
```

Send prepared batches:

```bash
uv run experiment/eval_gpt.py --send
```

Check active batches:

```bash
uv run experiment/eval_gpt.py --check
```

Retrieve outputs:

```bash
uv run experiment/eval_gpt.py --retrieve
```

Run on `sample_disprop`:

```bash
uv run experiment/eval_gpt.py --prepare --mode sample_disprop
```

Results are written to:

```text
experiment/result/raw/<subject>/0x/<model>.xlsx
```

Temporary batch files are written to:

```text
experiment/gpt_temp/
```

## `eval_gemini.py`

This script evaluates the dataset with Gemini models using Gemini Files API and Gemini batch jobs.

### Default Models

The script currently evaluates:

- `gemini-2.5-flash`
- `gemini-2.5-pro`

### Required Files

Before running, make sure these are available:

- `user_prompt.txt`
- `user_prompt_native.txt` for native-language mode
- experiment data under `sample/0x/<subject>/dataset.json`

API credentials are loaded from:

- `secrets/gemini_api_key.txt`

If that file is not present, the script falls back to environment variables supported by the Gemini SDK.

### Workflow

The Gemini pipeline has an extra image-upload stage because image files are uploaded first and then referenced in batch requests.

- `--upload_image`: upload local images to Gemini Files API
- `--prepare`: build `.jsonl` batch request files locally
- `--send`: submit prepared Gemini batch jobs
- `--check`: check active batch status
- `--retrieve`: download outputs and reconstruct Excel files
- `--debug`: process only instance `00`
- `--native`: use `user_prompt_native.txt` and native language prompting

The script also includes error-recovery stages:

- `--error_prepare`
- `--error_send`
- `--error_check`
- `--error_retrieve`

### Typical Usage

Upload images first:

```bash
uv run experiment/eval_gemini.py --upload_image
```

Prepare requests:

```bash
uv run experiment/eval_gemini.py --prepare
```

Prepare requests in native-language mode:

```bash
uv run experiment/eval_gemini.py --prepare --native
```

Send prepared batches:

```bash
uv run experiment/eval_gemini.py --send
```

Check active batches:

```bash
uv run experiment/eval_gemini.py --check
```

Retrieve outputs:

```bash
uv run experiment/eval_gemini.py --retrieve
```

### Notes

- Uploaded Gemini files expire, so `--upload_image` may need to be rerun before preparation.
- Native mode prefixes saved job/model keys with `NP_`.

Results are written to:

```text
experiment/result/raw/<subject>/0x/<model>.xlsx
```

Temporary Gemini files are written to:

```text
experiment/gemini_temp/
```

## `eval_openrouter.py`

This script evaluates the dataset through OpenRouter using a synchronous request loop, then extracts saved JSON responses into Excel files.

### Required Arguments

This script requires a model name on every run:

```bash
uv run experiment/eval_openrouter.py --model <model_name> ...
```

Example model values used by the script include:

- `qwen/qwen3.5-122b-a10b`
- `qwen/qwen3.5-27b`
- `meta-llama/llama-4-scout`
- `google/gemma-3-27b-it`

### Required Files

Before running, make sure these are available:

- `user_prompt.txt`
- `image_temp/image_urls.json`
- experiment data under `sample/0x/<subject>/dataset.json`
- `secrets/openrouter_api_key.txt`

For disproportionality mode, the script uses:

- `image_temp/image_urls_disprop.json`
- `sample_disprop/`
- subjects `math_original` and `math_disprop`

### Workflow

The OpenRouter pipeline has two stages:

- `--process`: run inference and save raw JSON responses
- `--extract`: parse saved responses and build Excel files
- `--debug`: process only instance `00`
- `--disprop`: run on the disproportionality dataset

### Typical Usage

Run inference:

```bash
uv run experiment/eval_openrouter.py --model qwen/qwen3.5-27b --process
```

Extract Excel outputs:

```bash
uv run experiment/eval_openrouter.py --model qwen/qwen3.5-27b --extract
```

Run in disproportionality mode:

```bash
uv run experiment/eval_openrouter.py --model qwen/qwen3.5-27b --process --disprop
```

### Output

Results are written to:

```text
experiment/result/raw/<subject>/0x/<model>.xlsx
```

Temporary OpenRouter tracking files are written to:

```text
experiment/openrouter_temp/
```
