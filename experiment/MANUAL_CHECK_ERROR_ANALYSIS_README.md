# Manual-Check Error Analysis Notes

This note documents how `manual_check_error_analysis.py` computes English-only perturbation-type error summaries, so future agents do not confuse full-sample GPT-5.4 failure analysis with the manual-check hard-problem subset.

## Source Files

- `experiment/sample/master_dataset.xlsx`
  - Ground-truth dataset annotation.
  - Has 10 sheets: `Instance_00` through `Instance_09`.
  - Each row has fields such as `subject`, `problem_id`, `question_type`, `answer`, `reasoning`, image path, and multilingual descriptions.
  - It does not contain per-model correctness columns such as `Correct`, `Accuracy`, or `Verdict`.

- `experiment/result/process/perturbation_type_manual_labels.tsv`
  - Manual-check perturbation label file.
  - Maps selected hard templates to `Perturbation_Type`.
  - Also has a manually recorded `Pass_Rate` and `Manual_Rationale`.
  - The `Pass_Rate` values match the analyzer notebook's GPT-5.4 English-only hard-problem pass rates.

- `experiment/result/process/eval_df_cache.pkl`
  - Cached model-evaluation table.
  - Columns: `Model`, `Subject`, `Language`, `Problem_ID`, `Instance`, `Accuracy`, `Display_Value`.
  - `Accuracy` is already a 0/1 correctness value.
  - This cache follows the analyzer notebook's grading pattern: parse each raw model response's `short answer`, then grade it against that row's `answer`.

- `experiment/analyzer.ipynb`
  - Canonical notebook for this analysis family.
  - Loads raw model output spreadsheets from `experiment/result/raw/**`.
  - Filters `excluded_class.txt`.
  - Grades model responses into an `eval_df` with `Accuracy`.
  - Its hard-problem export uses `target_model = "gpt-5_4-2026-03-05"` and `Language == "English"`.

- `experiment/result/process/analyzed_explicit/gpt5_4_correctness_long.csv`
  - Explicit GPT-5.4 correctness export.
  - Columns: `Subject`, `Language`, `Problem_ID`, `Instance`, `Predicted_Answer`, `Correct`, `Accuracy`.
  - Use this when the question is specifically about GPT-5.4 and an explicit correctness annotation is preferred.

- `experiment/excluded_class.txt`
  - Problem IDs that should be excluded before computing summaries.

## Important Distinction

`master_dataset.xlsx` is annotated with the ground truth, not with model correctness. It tells us the correct `answer` and reasoning for each generated instance. It does not directly say whether GPT-5.4, Gemini, InternVL, or any other model was correct.

For model correctness, use `eval_df_cache.pkl` or a model-specific explicit correctness export such as `gpt5_4_correctness_long.csv`.

## Main Counting Rule: English Only

For the full GPT-5.4 failure analysis, `manual_check_error_analysis.py`:

1. Loads excluded problem IDs from `experiment/excluded_class.txt`.
2. Loads all perturbation labels from `perturbation_type_all_labels.tsv`.
3. Removes excluded problem IDs from the labels.
4. Loads model correctness rows from `eval_df_cache.pkl`.
5. Filters to `Model == "gpt-5_4-2026-03-05"`.
6. Filters to `Language == "English"`.
7. Joins correctness rows to all perturbation labels on:
   - `Subject`
   - `Problem_ID`
8. Groups by `Perturbation_Type`.

One counted sample is:

```text
one GPT-5.4 English problem template x one instance
```

For each perturbation type:

```text
templates = unique Problem_ID count
samples = number of joined correctness rows
correct = sum(Accuracy)
errors = samples - correct
accuracy = correct / samples
error_rate = errors / samples
failure_share = errors / total GPT-5.4 English errors
```

## Full GPT-5.4 English Failure Result

Use this table to answer: from all GPT-5.4 English failures, which perturbation type is causing them?

```text
Perturbation   Samples  Correct  Errors  Accuracy  Error   Failure share
color             100       63      37     63.0%   37.0%          8.0%
shape           1,520    1,385     135     91.1%    8.9%         29.2%
pattern         1,540    1,423     117     92.4%    7.6%         25.3%
function_type   1,270    1,185      85     93.3%    6.7%         18.4%
numerical       1,630    1,541      89     94.5%    5.5%         19.2%
```

Interpretation:

- Highest conditional error rate: `color` at 37.0%.
- Largest share of total failures: `shape` at 29.2% of GPT-5.4 English failures.
- If the question is "which perturbation caused the most failures by count?", answer `shape`, followed by `pattern`.

## Manual-Check GPT-5.4 English Result

The manual-check hard-problem subset is separate. It comes from `perturbation_type_manual_labels.tsv`, which is based on `analyzer.ipynb` hard-problem output.

```text
color:          43 / 80 correct = 53.8% accuracy
shape:         205 / 340 correct = 60.3% accuracy
pattern:       203 / 320 correct = 63.4% accuracy
numerical:     171 / 260 correct = 65.8% accuracy
function_type: 255 / 340 correct = 75.0% accuracy
```

For the manual-check hard-problem subset, `color` is the most affected perturbation type by conditional error rate.

## Manual Pass-Rate Summary

The script also computes a separate manual-label-only summary from the `Pass_Rate` column:

```text
mean_pass_rate = average of Pass_Rate values within each Perturbation_Type
mean_error_rate = 1 - mean_pass_rate
```

This summary does not use per-model correctness rows. It only summarizes the manual TSV's `Pass_Rate` column.

## Current Output Location

Generated analysis files are written to:

```text
experiment/result/process/manual_check_error_analysis_english_excluded/
```

That directory is ignored by git via `experiment/result/process/`, so this README is the tracked reference for future agents.
