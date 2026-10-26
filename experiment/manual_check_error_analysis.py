from __future__ import annotations

from pathlib import Path

import pandas as pd


EXPERIMENT_ROOT = Path(__file__).resolve().parent
PROCESS_DIR = EXPERIMENT_ROOT / "result" / "process"
MANUAL_LABELS_PATH = PROCESS_DIR / "perturbation_type_manual_labels.tsv"
ALL_LABELS_PATH = PROCESS_DIR / "perturbation_type_all_labels.tsv"
EVAL_CACHE_PATH = PROCESS_DIR / "eval_df_cache.pkl"
EXCLUDED_CLASSES_PATH = EXPERIMENT_ROOT / "excluded_class.txt"
OUT_DIR = PROCESS_DIR / "manual_check_error_analysis_english_excluded"
LANGUAGE_FILTER = "English"
ANALYZER_TARGET_MODEL = "gpt-5_4-2026-03-05"

PERTURBATION_TYPE_ORDER = [
    "color",
    "pattern",
    "shape",
    "numerical",
    "function_type",
]

EXCLUDED_MODELS = {
    "Qwen_Qwen3_5-9B",
    "NP_gemini-2_5-flash",
    "NP_gemini-2_5-pro",
}

SELECTED_MODELS = [
    ANALYZER_TARGET_MODEL,
    "gemini-2_5-pro",
    "OpenGVLab_InternVL3_5-8B",
    "aisingapore_Qwen-SEA-LION-v4-8B-VL",
]

MODEL_DISPLAY_NAMES = {
    "OpenGVLab_InternVL3_5-8B": "InternVL3.5-8B",
    "aisingapore_Qwen-SEA-LION-v4-8B-VL": "SEA-LION-v4-8B-VL",
    "gemini-2_5-pro": "Gemini-2.5-Pro",
    "gpt-5_4-2026-03-05": "GPT-5.4",
}


def load_excluded_problem_ids() -> set[str]:
    if not EXCLUDED_CLASSES_PATH.exists():
        return set()
    return {
        line.strip()
        for line in EXCLUDED_CLASSES_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }


def parse_percent(series: pd.Series) -> pd.Series:
    return series.astype(str).str.rstrip("%").astype(float) / 100.0


def ordered_type_frame(df: pd.DataFrame) -> pd.DataFrame:
    order = {name: idx for idx, name in enumerate(PERTURBATION_TYPE_ORDER)}
    return (
        df.assign(_order=df["Perturbation_Type"].map(order).fillna(len(order)))
        .sort_values(["error_rate", "_order"], ascending=[False, True])
        .drop(columns=["_order"])
    )


def summarize_accuracy(df: pd.DataFrame, group_cols: list[str]) -> pd.DataFrame:
    summary = (
        df.groupby(group_cols, as_index=False)
        .agg(
            templates=("Problem_ID", lambda values: values.drop_duplicates().size),
            samples=("Accuracy", "size"),
            correct=("Accuracy", "sum"),
            accuracy=("Accuracy", "mean"),
        )
    )
    summary["errors"] = summary["samples"] - summary["correct"]
    summary["error_rate"] = 1.0 - summary["accuracy"]
    return summary


def add_failure_share(summary: pd.DataFrame) -> pd.DataFrame:
    total_errors = summary["errors"].sum()
    if total_errors == 0:
        summary["failure_share"] = 0.0
    else:
        summary["failure_share"] = summary["errors"] / total_errors
    return summary


def summarize_manual_pass_rates(manual_df: pd.DataFrame) -> pd.DataFrame:
    manual_df = manual_df.copy()
    manual_df["Pass_Rate_Value"] = parse_percent(manual_df["Pass_Rate"])
    summary = (
        manual_df.groupby("Perturbation_Type", as_index=False)
        .agg(
            templates=("Problem_ID", "count"),
            mean_pass_rate=("Pass_Rate_Value", "mean"),
            median_pass_rate=("Pass_Rate_Value", "median"),
            min_pass_rate=("Pass_Rate_Value", "min"),
            max_pass_rate=("Pass_Rate_Value", "max"),
        )
    )
    summary["mean_error_rate"] = 1.0 - summary["mean_pass_rate"]
    return (
        summary.rename(columns={"mean_error_rate": "error_rate"})
        .pipe(ordered_type_frame)
        .rename(columns={"error_rate": "mean_error_rate"})
    )


def format_percent(value: float) -> str:
    return f"{value * 100:.1f}%"


def sort_selected_model_summary(summary: pd.DataFrame) -> pd.DataFrame:
    model_order = {
        MODEL_DISPLAY_NAMES.get(model_name, model_name): idx
        for idx, model_name in enumerate(SELECTED_MODELS)
    }
    return (
        summary.assign(
            _model_order=summary["Model_Display"].map(model_order).fillna(len(model_order))
        )
        .sort_values(["_model_order", "error_rate"], ascending=[True, False])
        .drop(columns=["_model_order"])
    )


def sort_subject_summary(summary: pd.DataFrame) -> pd.DataFrame:
    return summary.sort_values(
        ["Subject", "error_rate", "Perturbation_Type"],
        ascending=[True, False, True],
    )


def write_markdown_report(
    out_path: Path,
    *,
    excluded_problem_ids: set[str],
    manual_overlap: set[str],
    manual_summary: pd.DataFrame,
    target_model_all_sample_summary: pd.DataFrame,
    target_model_summary: pd.DataFrame,
    eval_summary: pd.DataFrame,
    full_summary: pd.DataFrame,
) -> None:
    strongest_all_sample_rate = target_model_all_sample_summary.iloc[0]
    strongest_all_sample_count = target_model_all_sample_summary.sort_values(
        ["failure_share", "errors"],
        ascending=[False, False],
    ).iloc[0]
    strongest_manual = manual_summary.iloc[0]
    strongest_target = target_model_summary.iloc[0]
    strongest_eval = eval_summary.iloc[0]

    lines = [
        "# GPT-5.4 English Perturbation Failure Analysis",
        "",
        (
            "Primary scope: all GPT-5.4 English samples after excluded-class filtering, "
            "joined to the full perturbation label file."
        ),
        (
            "Secondary scope: analyzer-compatible manual-check hard-problem subset, "
            "plus all-model English-only comparisons."
        ),
        f"Excluded-class filter: {len(excluded_problem_ids)} IDs loaded from `experiment/excluded_class.txt`.",
        f"Manual-label overlap with excluded IDs: {len(manual_overlap)}.",
        "",
        "## Main Takeaway",
        "",
        (
            "For all GPT-5.4 English samples, "
            f"`{strongest_all_sample_rate['Perturbation_Type']}` has the highest conditional "
            f"error rate ({format_percent(strongest_all_sample_rate['error_rate'])}), "
            f"but `{strongest_all_sample_count['Perturbation_Type']}` contributes the largest "
            f"share of actual failures ({format_percent(strongest_all_sample_count['failure_share'])})."
        ),
        "",
        "## GPT-5.4 English All-Sample Failure Summary",
        "",
        "| Rank | Perturbation | Samples | Correct | Errors | Accuracy | Error | Failure Share |",
        "| ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]

    for idx, row in enumerate(target_model_all_sample_summary.itertuples(index=False), start=1):
        lines.append(
            "| "
            f"{idx} | {row.Perturbation_Type} | {row.samples} | "
            f"{int(row.correct)} | {int(row.errors)} | {format_percent(row.accuracy)} | "
            f"{format_percent(row.error_rate)} | {format_percent(row.failure_share)} |"
        )

    lines.extend(
        [
            "",
            "## GPT-5.4 English Manual-Check Subset",
            "",
            "This is the analyzer hard-problem/manual-check subset, not the full dataset.",
            "",
            "| Rank | Perturbation | Templates | Samples | Correct | Accuracy | Error |",
            "| ---: | --- | ---: | ---: | ---: | ---: | ---: |",
        ]
    )

    for idx, row in enumerate(target_model_summary.itertuples(index=False), start=1):
        lines.append(
            "| "
            f"{idx} | {row.Perturbation_Type} | {row.templates} | {row.samples} | "
            f"{int(row.correct)} | {format_percent(row.accuracy)} | "
            f"{format_percent(row.error_rate)} |"
        )

    lines.extend(
        [
            "",
            "## Manual TSV Pass-Rate Summary",
            "",
            "This summarizes the `Pass_Rate` column from the manual TSV.",
            "",
            "| Rank | Perturbation | Templates | Mean Pass | Mean Error | Median Pass |",
            "| ---: | --- | ---: | ---: | ---: | ---: |",
        ]
    )

    for idx, row in enumerate(manual_summary.itertuples(index=False), start=1):
        lines.append(
            "| "
            f"{idx} | {row.Perturbation_Type} | {row.templates} | "
            f"{format_percent(row.mean_pass_rate)} | {format_percent(row.mean_error_rate)} | "
            f"{format_percent(row.median_pass_rate)} |"
        )

    lines.extend(
        [
            "",
            "## All-Model English-Only Summary On Manual Labels",
            "",
            "| Rank | Perturbation | Templates | Samples | Accuracy | Error |",
            "| ---: | --- | ---: | ---: | ---: | ---: |",
        ]
    )

    for idx, row in enumerate(eval_summary.itertuples(index=False), start=1):
        lines.append(
            "| "
            f"{idx} | {row.Perturbation_Type} | {row.templates} | {row.samples} | "
            f"{format_percent(row.accuracy)} | {format_percent(row.error_rate)} |"
        )

    lines.extend(
        [
            "",
            "## Full Label Sanity Check",
            "",
            "This uses all perturbation labels and all non-excluded models, English only.",
            "",
            "| Rank | Perturbation | Templates | Samples | Accuracy | Error |",
            "| ---: | --- | ---: | ---: | ---: | ---: |",
        ]
    )
    for idx, row in enumerate(full_summary.itertuples(index=False), start=1):
        lines.append(
            "| "
            f"{idx} | {row.Perturbation_Type} | {row.templates} | {row.samples} | "
            f"{format_percent(row.accuracy)} | {format_percent(row.error_rate)} |"
        )

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    excluded_problem_ids = load_excluded_problem_ids()
    manual_df = pd.read_csv(MANUAL_LABELS_PATH, sep="\t")
    manual_overlap = set(manual_df["Problem_ID"]) & excluded_problem_ids
    manual_df = manual_df[~manual_df["Problem_ID"].isin(excluded_problem_ids)].copy()

    eval_df = pd.read_pickle(EVAL_CACHE_PATH)
    eval_df = eval_df[
        ~eval_df["Problem_ID"].isin(excluded_problem_ids)
        & ~eval_df["Model"].isin(EXCLUDED_MODELS)
        & (eval_df["Language"] == LANGUAGE_FILTER)
    ].copy()

    manual_labels_df = manual_df[["Subject", "Problem_ID", "Perturbation_Type"]].copy()
    manual_eval_df = eval_df.merge(
        manual_labels_df,
        on=["Subject", "Problem_ID"],
        how="inner",
    )

    all_labels_df = pd.read_csv(ALL_LABELS_PATH, sep="\t")
    all_labels_df = all_labels_df[
        ~all_labels_df["Problem_ID"].isin(excluded_problem_ids)
    ].copy()
    full_eval_df = eval_df.merge(
        all_labels_df[["Subject", "Problem_ID", "Perturbation_Type"]],
        on=["Subject", "Problem_ID"],
        how="inner",
    )

    manual_summary = summarize_manual_pass_rates(manual_df)
    target_model_all_sample_summary = add_failure_share(
        ordered_type_frame(
            summarize_accuracy(
                full_eval_df[full_eval_df["Model"] == ANALYZER_TARGET_MODEL],
                ["Perturbation_Type"],
            )
        )
    )
    target_model_summary = ordered_type_frame(
        summarize_accuracy(
            manual_eval_df[manual_eval_df["Model"] == ANALYZER_TARGET_MODEL],
            ["Perturbation_Type"],
        )
    )
    eval_summary = ordered_type_frame(
        summarize_accuracy(manual_eval_df, ["Perturbation_Type"])
    )
    selected_model_summary = sort_selected_model_summary(
        summarize_accuracy(
            manual_eval_df[manual_eval_df["Model"].isin(SELECTED_MODELS)].assign(
                Model_Display=lambda df: df["Model"].map(MODEL_DISPLAY_NAMES).fillna(df["Model"])
            ),
            ["Model_Display", "Perturbation_Type"],
        )
    )
    subject_summary = sort_subject_summary(
        summarize_accuracy(manual_eval_df, ["Subject", "Perturbation_Type"])
    )
    full_summary = ordered_type_frame(
        summarize_accuracy(full_eval_df, ["Perturbation_Type"])
    )

    manual_ranked = manual_df.copy()
    manual_ranked["Pass_Rate_Value"] = parse_percent(manual_ranked["Pass_Rate"])
    manual_ranked["Error_Rate_Value"] = 1.0 - manual_ranked["Pass_Rate_Value"]
    manual_ranked = manual_ranked.sort_values(
        ["Error_Rate_Value", "Subject", "Problem_ID"],
        ascending=[False, True, True],
    )

    manual_summary.to_csv(OUT_DIR / "manual_pass_rate_by_perturbation.csv", index=False)
    target_model_all_sample_summary.to_csv(
        OUT_DIR / "gpt5_4_english_all_sample_failure_by_perturbation.csv",
        index=False,
    )
    target_model_summary.to_csv(
        OUT_DIR / "gpt5_4_english_error_by_perturbation.csv",
        index=False,
    )
    eval_summary.to_csv(
        OUT_DIR / "all_model_english_error_by_perturbation_manual_labels.csv",
        index=False,
    )
    selected_model_summary.to_csv(
        OUT_DIR / "selected_model_english_error_by_perturbation.csv",
        index=False,
    )
    subject_summary.to_csv(OUT_DIR / "subject_english_error_by_perturbation.csv", index=False)
    full_summary.to_csv(
        OUT_DIR / "full_label_english_error_by_perturbation.csv",
        index=False,
    )
    manual_ranked.to_csv(OUT_DIR / "manual_templates_ranked_by_error.csv", index=False)

    with pd.ExcelWriter(OUT_DIR / "manual_check_error_analysis_english_excluded.xlsx") as writer:
        target_model_all_sample_summary.to_excel(
            writer,
            sheet_name="gpt5_4_all_samples",
            index=False,
        )
        target_model_summary.to_excel(writer, sheet_name="gpt5_4_english", index=False)
        manual_summary.to_excel(writer, sheet_name="manual_pass_rate", index=False)
        eval_summary.to_excel(writer, sheet_name="all_model_english", index=False)
        selected_model_summary.to_excel(writer, sheet_name="selected_models", index=False)
        subject_summary.to_excel(writer, sheet_name="subject_type", index=False)
        full_summary.to_excel(writer, sheet_name="full_label_check", index=False)
        manual_ranked.to_excel(writer, sheet_name="manual_templates", index=False)

    write_markdown_report(
        OUT_DIR / "README.md",
        excluded_problem_ids=excluded_problem_ids,
        manual_overlap=manual_overlap,
        manual_summary=manual_summary,
        target_model_all_sample_summary=target_model_all_sample_summary,
        target_model_summary=target_model_summary,
        eval_summary=eval_summary,
        full_summary=full_summary,
    )

    print(f"Wrote manual-check perturbation analysis to {OUT_DIR}")


if __name__ == "__main__":
    main()
