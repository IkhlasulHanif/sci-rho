from __future__ import annotations

from pathlib import Path
import re

import pandas as pd


EXPERIMENT_ROOT = Path(__file__).resolve().parents[1]
PROCESS_DIR = EXPERIMENT_ROOT / "result" / "process"
AVG_XLSX_PATH = PROCESS_DIR / "average_accuracy.xlsx"
WC_XLSX_PATH = PROCESS_DIR / "worst_case_accuracy.xlsx"
DEFAULT_LATEX_OUT_DIR = EXPERIMENT_ROOT / "result" / "tables" / "latex"


LANGUAGE_ORDER = [
    "English",
    "Arabic",
    "Chinese",
    "Hindi",
    "Indonesian",
    "Kazakh",
    "Swahili",
]

SUBJECT_ORDER = [
    "Mathematics",
    "Physics",
    "Chemistry",
    "Biology",
    "Compsci",
]

MODEL_DISPLAY_NAMES = {
    "OpenGVLab_InternVL3_5-14B": "InternVL3.5-14B",
    "OpenGVLab_InternVL3_5-8B": "InternVL3.5-8B",
    "OpenGVLab_InternVL3_5-4B": "InternVL3.5-4B",
    "Qwen_Qwen3-VL-4B-Instruct": "Qwen3-VL-4B-Instruct",
    "Qwen_Qwen3-VL-8B-Instruct": "Qwen3-VL-8B-Instruct",
    "Qwen_Qwen3_5-9B": "Qwen3.5-9B",
    "aisingapore_Qwen-SEA-LION-v4-4B-VL": "SEA-LION-v4-4B-VL",
    "aisingapore_Qwen-SEA-LION-v4-8B-VL": "SEA-LION-v4-8B-VL",
    "allenai_Molmo2-4B": "Molmo2-4B",
    "allenai_Molmo2-8B": "Molmo2-8B",
    "gemini-2_5-flash": "Gemini-2.5-Flash",
    "gemini-2_5-pro": "Gemini-2.5-Pro",
    "google_gemma-3-12b-it": "Gemma-3-12B-IT",
    "google_gemma-3-4b-it": "Gemma-3-4B-IT",
    "gpt-5_4-2026-03-05": "GPT-5.4",
    "meta-llama_llama-4-scout": "Llama-4-Scout",
    "qwen_qwen3_5-122b-a10b": "Qwen3.5-122B-A10B",
}

MODEL_GROUPS = {
    "closed_source": [
        "gpt-5_4-2026-03-05",
        "gemini-2_5-pro",
        "gemini-2_5-flash",
    ],
    "open_source": [
        "qwen_qwen3_5-122b-a10b",
        "meta-llama_llama-4-scout",
        "OpenGVLab_InternVL3_5-14B",
        "OpenGVLab_InternVL3_5-8B",
        "OpenGVLab_InternVL3_5-4B",
        "Qwen_Qwen3-VL-8B-Instruct",
        "Qwen_Qwen3-VL-4B-Instruct",
        "allenai_Molmo2-8B",
        "allenai_Molmo2-4B",
        "google_gemma-3-12b-it",
        "google_gemma-3-4b-it",
        "aisingapore_Qwen-SEA-LION-v4-8B-VL",
        "aisingapore_Qwen-SEA-LION-v4-4B-VL",
    ],
}

GROUP_TITLES = {
    "closed_source": "Closed-source Models",
    "open_source": "Open-source Models",
}

EXCLUDED_MODELS = {
    "Qwen_Qwen3_5-9B",
    "NP_gemini-2_5-flash",
    "NP_gemini-2_5-pro",
}


def _escape_latex(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    pattern = re.compile("|".join(re.escape(key) for key in replacements))
    return pattern.sub(lambda match: replacements[match.group(0)], str(text))


def _format_metric_value(value: float | int | None, decimals: int = 1) -> str:
    if pd.isna(value):
        return "--"
    return f"{float(value) * 100:.{decimals}f}"


def _display_model_name(model_name: str) -> str:
    return MODEL_DISPLAY_NAMES.get(model_name, model_name.replace("_", "-"))


def _compute_average_accuracy(eval_df: pd.DataFrame) -> pd.DataFrame:
    return (
        eval_df.groupby(["Model", "Subject", "Language"])["Accuracy"]
        .mean()
        .reset_index()
    )


def _compute_worst_case_accuracy(eval_df: pd.DataFrame) -> pd.DataFrame:
    per_problem = (
        eval_df.groupby(["Model", "Subject", "Language", "Problem_ID"])["Accuracy"]
        .min()
        .reset_index()
    )
    return (
        per_problem.groupby(["Model", "Subject", "Language"])["Accuracy"]
        .mean()
        .reset_index()
    )


def _compute_reasoning_robustness(eval_df: pd.DataFrame) -> pd.DataFrame:
    avg_df = _compute_average_accuracy(eval_df)
    wc_df = _compute_worst_case_accuracy(eval_df)
    merged = avg_df.merge(
        wc_df,
        on=["Model", "Subject", "Language"],
        suffixes=("_avg", "_wc"),
        how="outer",
    )
    merged["Accuracy"] = (
        merged["Accuracy_wc"] / merged["Accuracy_avg"]
    ).replace([float("inf"), float("-inf")], pd.NA)
    merged["Accuracy"] = merged["Accuracy"].fillna(0)
    return merged[["Model", "Subject", "Language", "Accuracy"]]


def _summarize_for_dimension(
    metric_df: pd.DataFrame,
    dimension: str,
    order: list[str],
) -> pd.DataFrame:
    summary = (
        metric_df.groupby(["Model", dimension])["Accuracy"]
        .mean()
        .reset_index()
        .pivot(index="Model", columns=dimension, values="Accuracy")
    )

    ordered_columns = [col for col in order if col in summary.columns]
    remaining_columns = sorted(col for col in summary.columns if col not in ordered_columns)
    summary = summary.reindex(columns=ordered_columns + remaining_columns)

    overall = metric_df.groupby("Model")["Accuracy"].mean().rename("ALL")
    summary.insert(0, "ALL", overall.reindex(summary.index))
    return summary.sort_index()


def _load_metric_pivot(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Missing metric file: {path}")
    pivot = pd.read_excel(path, header=[0, 1], index_col=0)
    pivot.index = pivot.index.astype(str)
    pivot = pivot.loc[~pivot.index.isin(EXCLUDED_MODELS)]
    return pivot


def _summarize_pivot_for_dimension(
    metric_pivot: pd.DataFrame,
    dimension: str,
    order: list[str],
) -> pd.DataFrame:
    if dimension == "Language":
        summary = metric_pivot.T.groupby(level=1).mean().T
    elif dimension == "Subject":
        summary = metric_pivot.T.groupby(level=0).mean().T
    else:
        raise ValueError(f"Unsupported dimension: {dimension}")

    ordered_columns = [col for col in order if col in summary.columns]
    remaining_columns = sorted(col for col in summary.columns if col not in ordered_columns)
    summary = summary.reindex(columns=ordered_columns + remaining_columns)

    summary.insert(0, "ALL", metric_pivot.mean(axis=1))
    return summary.sort_index()


def build_latex_table(
    summary_df: pd.DataFrame,
    caption: str,
    label: str,
    first_column_name: str = "Model",
    decimals: int = 1,
    grouped_rows: bool = False,
) -> str:
    summary_df = summary_df.loc[~summary_df.index.isin(EXCLUDED_MODELS)]
    headers = [first_column_name] + list(summary_df.columns)
    col_spec = "l" + ("r" * len(summary_df.columns))

    lines = [
        r"\begin{table}[h]",
        r"\centering",
        rf"\caption{{{caption}}}",
        rf"\label{{{label}}}",
        r"\resizebox{\textwidth}{!}{%",
        rf"\begin{{tabular}}{{{col_spec}}}",
        r"\hline",
        " & ".join(rf"\textbf{{{_escape_latex(header)}}}" for header in headers) + r" \\",
        r"\hline",
    ]

    if grouped_rows:
        rendered_models: set[str] = set()
        ordered_groups = tuple(MODEL_GROUPS.keys())
        for idx, group_name in enumerate(ordered_groups):
            group_models = [
                model_name for model_name in MODEL_GROUPS[group_name]
                if model_name in summary_df.index
            ]
            if not group_models:
                continue
            if group_name != "sea_lion":
                lines.append(
                    rf"\multicolumn{{{len(headers)}}}{{c}}{{\textit{{{_escape_latex(GROUP_TITLES[group_name])}}}}} \\"
                )
                lines.append(r"\hline")
            for model_name in group_models:
                row = summary_df.loc[model_name]
                values = [_escape_latex(_display_model_name(model_name))]
                values.extend(_format_metric_value(row[col], decimals=decimals) for col in summary_df.columns)
                lines.append(" & ".join(values) + r" \\")
                rendered_models.add(model_name)
            if idx < len(ordered_groups) - 1:
                lines.append(r"\hline")
                lines.append(rf"\multicolumn{{{len(headers)}}}{{l}}{{}} \\")

        remaining_models = [model_name for model_name in summary_df.index if model_name not in rendered_models]
        for model_name in remaining_models:
            row = summary_df.loc[model_name]
            values = [_escape_latex(_display_model_name(model_name))]
            values.extend(_format_metric_value(row[col], decimals=decimals) for col in summary_df.columns)
            lines.append(" & ".join(values) + r" \\")
    else:
        for model_name, row in summary_df.iterrows():
            values = [_escape_latex(_display_model_name(model_name))]
            values.extend(_format_metric_value(row[col], decimals=decimals) for col in summary_df.columns)
            lines.append(" & ".join(values) + r" \\")

    lines.extend(
        [
            r"\hline",
            r"\end{tabular}%",
            r"}",
            r"\end{table}",
        ]
    )
    return "\n".join(lines)


def build_combined_english_table(
    eval_df: pd.DataFrame,
    caption: str,
    label: str,
    decimals: int = 1,
) -> str:
    english_df = eval_df[eval_df["Language"] == "English"].copy()
    english_df = english_df[~english_df["Model"].isin(EXCLUDED_MODELS)]
    if english_df.empty:
        raise ValueError("No English rows found for combined English LaTeX table.")

    avg_df = _compute_average_accuracy(english_df)
    wc_df = _compute_worst_case_accuracy(english_df)

    avg_pivot = (
        avg_df.pivot(index="Model", columns="Subject", values="Accuracy")
        .reindex(columns=[col for col in SUBJECT_ORDER if col in avg_df["Subject"].unique()])
    )
    wc_pivot = (
        wc_df.pivot(index="Model", columns="Subject", values="Accuracy")
        .reindex(columns=[col for col in SUBJECT_ORDER if col in wc_df["Subject"].unique()])
    )
    delta_pivot = wc_pivot - avg_pivot

    subjects = list(avg_pivot.columns)
    headers_top = ["Model"]
    headers_bottom = [""]
    for subject in subjects:
        headers_top.append(rf"\multicolumn{{3}}{{c}}{{\textbf{{{_escape_latex(subject)}}}}}")
        headers_bottom.extend([r"$A_{avg}$", r"$A_{wst}$", r"$\Delta$"])

    col_spec = "l|" + "|".join("rrc" for _ in subjects)
    lines = [
        r"\begin{table}[h]",
        r"\centering",
        rf"\caption{{{caption}}}",
        rf"\label{{{label}}}",
        r"\resizebox{\textwidth}{!}{%",
        rf"\begin{{tabular}}{{{col_spec}}}",
        r"\hline",
        r"\textbf{Model} & " + " & ".join(headers_top[1:]) + r" \\",
        " & ".join(headers_bottom) + r" \\",
        r"\hline",
    ]

    rendered_models: set[str] = set()
    ordered_groups = ("closed_source", "open_source")
    for idx, group_name in enumerate(ordered_groups):
        group_models = [model_name for model_name in MODEL_GROUPS[group_name] if model_name in avg_pivot.index]
        if not group_models:
            continue
        lines.append(
            rf"\multicolumn{{{1 + 3 * len(subjects)}}}{{c}}{{\textit{{{_escape_latex(GROUP_TITLES[group_name])}}}}} \\"
        )
        lines.append(r"\hline")
        for model_name in group_models:
            row = [_escape_latex(_display_model_name(model_name))]
            for subject in subjects:
                row.append(_format_metric_value(avg_pivot.loc[model_name, subject], decimals=decimals))
                row.append(_format_metric_value(wc_pivot.loc[model_name, subject], decimals=decimals))
                row.append(_format_metric_value(delta_pivot.loc[model_name, subject], decimals=decimals))
            lines.append(" & ".join(row) + r" \\")
            rendered_models.add(model_name)
        if idx < len(ordered_groups) - 1:
            lines.append(r"\hline")
            lines.append(rf"\multicolumn{{{1 + 3 * len(subjects)}}}{{l}}{{}} \\")

    remaining_models = [model_name for model_name in avg_pivot.index if model_name not in rendered_models]
    for model_name in remaining_models:
        row = [_escape_latex(_display_model_name(model_name))]
        for subject in subjects:
            row.append(_format_metric_value(avg_pivot.loc[model_name, subject], decimals=decimals))
            row.append(_format_metric_value(wc_pivot.loc[model_name, subject], decimals=decimals))
            row.append(_format_metric_value(delta_pivot.loc[model_name, subject], decimals=decimals))
        lines.append(" & ".join(row) + r" \\")

    lines.extend(
        [
            r"\hline",
            r"\end{tabular}%",
            r"}",
            r"\end{table}",
        ]
    )
    return "\n".join(lines)


def export_latex_tables(eval_df: pd.DataFrame, out_dir: Path | str) -> list[Path]:
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    for legacy_file in out_path.glob("*.tex"):
        legacy_file.unlink()

    total_questions = (
        eval_df[["Subject", "Problem_ID", "Instance"]]
        .drop_duplicates()
        .shape[0]
    )

    metric_builders = {
        "average_case_accuracy": (
            _compute_average_accuracy(eval_df),
            r"Average-case accuracy ($\times 100$)",
        ),
        "worst_case_accuracy": (
            _compute_worst_case_accuracy(eval_df),
            r"Worst-case accuracy ($\times 100$)",
        ),
    }

    dimension_specs = {
        "language": ("Language", LANGUAGE_ORDER),
        "subject": ("Subject", SUBJECT_ORDER),
    }

    saved_paths: list[Path] = []

    for metric_slug, (metric_df, metric_title) in metric_builders.items():
        for dimension_slug, (dimension_name, order) in dimension_specs.items():
            summary_df = _summarize_for_dimension(metric_df, dimension_name, order)
            grouping_phrase = (
                "averaged over all subjects"
                if dimension_name == "Language"
                else "averaged over all languages"
            )
            caption = (
                f"{metric_title} on STEM-Vision with {total_questions:,} generated question instances. "
                f'"ALL" denotes the overall accuracy. The remaining columns report scores by '
                f"{dimension_name.lower()}, {grouping_phrase}."
            )
            label = f"tab:stem_vision_{metric_slug}_{dimension_slug}"
            latex = build_latex_table(
                summary_df=summary_df,
                caption=caption,
                label=label,
                grouped_rows=True,
            )

            file_path = out_path / f"stem_vision_{metric_slug}_by_{dimension_slug}.tex"
            file_path.write_text(latex + "\n", encoding="utf-8")
            saved_paths.append(file_path)

    combined_caption = (
        'English-only results on STEM-Vision. For each subject, '
        r'$A_{avg}$ denotes average-case accuracy ($\times 100$) and '
        r'$A_{wst}$ denotes worst-case accuracy ($\times 100$). '
        r'$\Delta$ denotes the reduction $A_{wst} - A_{avg}$ ($\times 100$).'
    )
    combined_latex = build_combined_english_table(
        eval_df=eval_df,
        caption=combined_caption,
        label="tab:stem_vision_english_avg_wc_by_subject",
    )
    combined_path = out_path / "stem_vision_english_avg_wc_by_subject.tex"
    combined_path.write_text(combined_latex + "\n", encoding="utf-8")
    saved_paths.append(combined_path)

    return saved_paths


def export_latex_tables_from_metric_files(
    avg_xlsx_path: Path | str = AVG_XLSX_PATH,
    wc_xlsx_path: Path | str = WC_XLSX_PATH,
    out_dir: Path | str = DEFAULT_LATEX_OUT_DIR,
) -> list[Path]:
    avg_pivot = _load_metric_pivot(Path(avg_xlsx_path))
    wc_pivot = _load_metric_pivot(Path(wc_xlsx_path))

    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    for legacy_file in out_path.glob("*.tex"):
        legacy_file.unlink()

    metric_builders = {
        "average_case_accuracy": (
            avg_pivot,
            r"Average-case accuracy ($\times 100$)",
        ),
        "worst_case_accuracy": (
            wc_pivot,
            r"Worst-case accuracy ($\times 100$)",
        ),
    }

    dimension_specs = {
        "language": ("Language", LANGUAGE_ORDER),
        "subject": ("Subject", SUBJECT_ORDER),
    }

    saved_paths: list[Path] = []

    for metric_slug, (metric_pivot, metric_title) in metric_builders.items():
        for dimension_slug, (dimension_name, order) in dimension_specs.items():
            summary_df = _summarize_pivot_for_dimension(metric_pivot, dimension_name, order)
            grouping_phrase = (
                "averaged over all subjects"
                if dimension_name == "Language"
                else "averaged over all languages"
            )
            caption = (
                f"{metric_title} on STEM-Vision. "
                f'"ALL" denotes the overall accuracy. The remaining columns report scores by '
                f"{dimension_name.lower()}, {grouping_phrase}."
            )
            label = f"tab:stem_vision_{metric_slug}_{dimension_slug}"
            latex = build_latex_table(
                summary_df=summary_df,
                caption=caption,
                label=label,
                grouped_rows=True,
            )

            file_path = out_path / f"stem_vision_{metric_slug}_by_{dimension_slug}.tex"
            file_path.write_text(latex + "\n", encoding="utf-8")
            saved_paths.append(file_path)

    english_avg = avg_pivot.xs("English", level=1, axis=1, drop_level=True)
    english_wc = wc_pivot.xs("English", level=1, axis=1, drop_level=True)
    english_avg = english_avg.reindex(columns=[col for col in SUBJECT_ORDER if col in english_avg.columns])
    english_wc = english_wc.reindex(columns=[col for col in SUBJECT_ORDER if col in english_wc.columns])
    english_delta = english_wc - english_avg

    subjects = list(english_avg.columns)
    headers_top = ["Model"]
    headers_bottom = [""]
    for subject in subjects:
        headers_top.append(rf"\multicolumn{{3}}{{c}}{{\textbf{{{_escape_latex(subject)}}}}}")
        headers_bottom.extend([r"$A_{avg}$", r"$A_{wst}$", r"$\Delta$"])

    col_spec = "l|" + "|".join("rrc" for _ in subjects)
    lines = [
        r"\begin{table}[h]",
        r"\centering",
        (
            r"\caption{English-only results on STEM-Vision. For each subject, "
            r"$A_{avg}$ denotes average-case accuracy ($\times 100$) and "
            r"$A_{wst}$ denotes worst-case accuracy ($\times 100$). "
            r"$\Delta$ denotes the reduction $A_{wst} - A_{avg}$ ($\times 100$).}"
        ),
        r"\label{tab:stem_vision_english_avg_wc_by_subject}",
        r"\resizebox{\textwidth}{!}{%",
        rf"\begin{{tabular}}{{{col_spec}}}",
        r"\hline",
        r"\textbf{Model} & " + " & ".join(headers_top[1:]) + r" \\",
        " & ".join(headers_bottom) + r" \\",
        r"\hline",
    ]

    rendered_models: set[str] = set()
    ordered_groups = ("closed_source", "open_source")
    for idx, group_name in enumerate(ordered_groups):
        group_models = [model_name for model_name in MODEL_GROUPS[group_name] if model_name in english_avg.index]
        if not group_models:
            continue
        lines.append(
            rf"\multicolumn{{{1 + 3 * len(subjects)}}}{{c}}{{\textit{{{_escape_latex(GROUP_TITLES[group_name])}}}}} \\"
        )
        lines.append(r"\hline")
        for model_name in group_models:
            row = [_escape_latex(_display_model_name(model_name))]
            for subject in subjects:
                row.append(_format_metric_value(english_avg.loc[model_name, subject]))
                row.append(_format_metric_value(english_wc.loc[model_name, subject]))
                row.append(_format_metric_value(english_delta.loc[model_name, subject]))
            lines.append(" & ".join(row) + r" \\")
            rendered_models.add(model_name)
        if idx < len(ordered_groups) - 1:
            lines.append(r"\hline")
            lines.append(rf"\multicolumn{{{1 + 3 * len(subjects)}}}{{l}}{{}} \\")

    remaining_models = [model_name for model_name in english_avg.index if model_name not in rendered_models]
    for model_name in remaining_models:
        row = [_escape_latex(_display_model_name(model_name))]
        for subject in subjects:
            row.append(_format_metric_value(english_avg.loc[model_name, subject]))
            row.append(_format_metric_value(english_wc.loc[model_name, subject]))
            row.append(_format_metric_value(english_delta.loc[model_name, subject]))
        lines.append(" & ".join(row) + r" \\")

    lines.extend(
        [
            r"\hline",
            r"\end{tabular}%",
            r"}",
            r"\end{table}",
        ]
    )
    combined_path = out_path / "stem_vision_english_avg_wc_by_subject.tex"
    combined_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    saved_paths.append(combined_path)

    return saved_paths


def main() -> None:
    saved_paths = export_latex_tables_from_metric_files()
    for path in saved_paths:
        print(path)


if __name__ == "__main__":
    main()
