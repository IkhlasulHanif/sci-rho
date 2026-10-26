from __future__ import annotations

from pathlib import Path
import re

import pandas as pd


EXPERIMENT_ROOT = Path(__file__).resolve().parents[1]
PROCESS_DIR = EXPERIMENT_ROOT / "result" / "process"
AVG_XLSX_PATH = PROCESS_DIR / "average_accuracy.xlsx"
WC_XLSX_PATH = PROCESS_DIR / "worst_case_accuracy.xlsx"
EVAL_CACHE_PATH = PROCESS_DIR / "eval_df_cache.pkl"
PERTURBATION_LABELS_PATH = PROCESS_DIR / "perturbation_type_all_labels.tsv"
EXCLUDED_CLASSES_PATH = EXPERIMENT_ROOT / "excluded_class.txt"
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

PERTURBATION_TYPE_ORDER = [
    "color",
    "function_type",
    "numerical",
    "pattern",
    "shape",
]

PERTURBATION_TYPE_DISPLAY_NAMES = {
    "color": "Color",
    "function_type": "Function type",
    "numerical": "Numerical",
    "pattern": "Pattern",
    "shape": "Shape",
}

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
    "qwen_qwen3_5-27b": "Qwen3.5-27B",
}

MODEL_GROUPS = {
    "closed_source": [
        "gpt-5_4-2026-03-05",
        "gemini-2_5-pro",
        "gemini-2_5-flash",
    ],
    "open_source": [
        "qwen_qwen3_5-122b-a10b",
        "qwen_qwen3_5-27b",
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

ROBUSTNESS_SUMMARY_MODELS = [
    "gpt-5_4-2026-03-05",
    "gemini-2_5-pro",
    "OpenGVLab_InternVL3_5-8B",
    "aisingapore_Qwen-SEA-LION-v4-8B-VL",
]


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


def _safe_accuracy_ratio(
    numerator: pd.DataFrame | pd.Series,
    denominator: pd.DataFrame | pd.Series,
) -> pd.DataFrame | pd.Series:
    ratio = numerator.divide(denominator)
    return ratio.replace([float("inf"), float("-inf")], pd.NA).fillna(0)


def _display_model_name(model_name: str) -> str:
    return MODEL_DISPLAY_NAMES.get(model_name, model_name.replace("_", "-"))


def _load_excluded_problem_ids(
    path: Path | str = EXCLUDED_CLASSES_PATH,
) -> set[str]:
    excluded_path = Path(path)
    if not excluded_path.exists():
        return set()
    return {
        line.strip()
        for line in excluded_path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }


def _filter_eval_df_to_stem_subjects(eval_df: pd.DataFrame) -> pd.DataFrame:
    filtered_df = eval_df[eval_df["Subject"].isin(SUBJECT_ORDER)].copy()
    excluded_problem_ids = _load_excluded_problem_ids()
    if excluded_problem_ids:
        filtered_df = filtered_df[
            ~filtered_df["Problem_ID"].isin(excluded_problem_ids)
        ].copy()
    return filtered_df


def _filter_pivot_to_stem_subjects(metric_pivot: pd.DataFrame) -> pd.DataFrame:
    if isinstance(metric_pivot.columns, pd.MultiIndex):
        keep_columns = metric_pivot.columns.get_level_values(0).isin(SUBJECT_ORDER)
        return metric_pivot.loc[:, keep_columns]
    keep_columns = [column for column in SUBJECT_ORDER if column in metric_pivot.columns]
    return metric_pivot.reindex(columns=keep_columns)


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
    merged["Accuracy"] = _safe_accuracy_ratio(merged["Accuracy_wc"], merged["Accuracy_avg"])
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
    return _filter_pivot_to_stem_subjects(pivot)


def _load_perturbation_labels(path: Path | str = PERTURBATION_LABELS_PATH) -> pd.DataFrame:
    labels_path = Path(path)
    if not labels_path.exists():
        raise FileNotFoundError(f"Missing perturbation label file: {labels_path}")

    labels_df = pd.read_csv(labels_path, sep="\t")
    required_columns = {"Subject", "Problem_ID", "Perturbation_Type"}
    missing_columns = required_columns - set(labels_df.columns)
    if missing_columns:
        raise ValueError(
            f"Perturbation label file is missing columns: {sorted(missing_columns)}"
        )

    duplicate_count = labels_df.duplicated(["Subject", "Problem_ID"]).sum()
    if duplicate_count:
        raise ValueError(
            f"Perturbation label file has {duplicate_count} duplicate template labels."
        )

    unknown_types = set(labels_df["Perturbation_Type"]) - set(PERTURBATION_TYPE_ORDER)
    if unknown_types:
        raise ValueError(
            f"Perturbation label file has unknown types: {sorted(unknown_types)}"
        )

    labels_df = labels_df[["Subject", "Problem_ID", "Perturbation_Type"]].copy()
    excluded_problem_ids = _load_excluded_problem_ids()
    if excluded_problem_ids:
        labels_df = labels_df[
            ~labels_df["Problem_ID"].isin(excluded_problem_ids)
        ].copy()
    return labels_df


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


def _ordered_models(model_index: pd.Index) -> list[str]:
    ordered_models: list[str] = []
    seen: set[str] = set()

    for group_name in MODEL_GROUPS:
        for model_name in MODEL_GROUPS[group_name]:
            if model_name in model_index and model_name not in seen:
                ordered_models.append(model_name)
                seen.add(model_name)

    ordered_models.extend(model_name for model_name in model_index if model_name not in seen)
    return ordered_models


def _metric_df_to_subject_language_pivot(metric_df: pd.DataFrame) -> pd.DataFrame:
    metric_df = metric_df[metric_df["Subject"].isin(SUBJECT_ORDER)].copy()
    pivot = metric_df.pivot(
        index="Model",
        columns=["Subject", "Language"],
        values="Accuracy",
    )
    pivot = pivot.loc[~pivot.index.isin(EXCLUDED_MODELS)]
    return pivot.sort_index()


def _language_columns(metric_pivot: pd.DataFrame, language: str | None) -> pd.Index:
    if language is None:
        return metric_pivot.columns
    return metric_pivot.columns[metric_pivot.columns.get_level_values(1) == language]


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


def build_selected_model_language_robustness_table(
    avg_pivot: pd.DataFrame,
    wc_pivot: pd.DataFrame,
    caption: str,
    label: str,
    decimals: int = 1,
) -> str:
    common_models = avg_pivot.index.intersection(wc_pivot.index)
    common_columns = avg_pivot.columns.intersection(wc_pivot.columns)
    selected_models = [
        model_name
        for model_name in ROBUSTNESS_SUMMARY_MODELS
        if model_name in common_models
    ]
    if not selected_models:
        raise ValueError("None of the selected robustness-summary models were found.")
    avg_common = avg_pivot.loc[selected_models, common_columns]
    wc_common = wc_pivot.loc[selected_models, common_columns]

    languages = ["ALL"] + [
        language
        for language in LANGUAGE_ORDER
        if language in avg_common.columns.get_level_values(1)
    ]

    lines = [
        r"\begin{table}[h]",
        r"\centering",
        rf"\caption{{{caption}}}",
        rf"\label{{{label}}}",
        r"\begin{tabular}{lrrrr}",
        r"\hline",
        r"\textbf{Language} & $A_{avg}$ & $A_{wst}$ & $\Delta$ & $\mathcal{R}$ \\",
        r"\hline",
    ]

    for model_idx, model_name in enumerate(selected_models):
        if model_idx > 0:
            lines.append(r"\hline")
        lines.append(
            rf"\multicolumn{{5}}{{c}}{{\textit{{{_escape_latex(_display_model_name(model_name))}}}}} \\"
        )
        lines.append(r"\hline")
        for language in languages:
            selected_language = None if language == "ALL" else language
            columns = _language_columns(avg_common, selected_language)
            avg_value = avg_common.loc[model_name, columns].mean()
            wc_value = wc_common.loc[model_name, columns].mean()
            delta_value = wc_value - avg_value
            robustness_value = 0.0 if avg_value == 0 else wc_value / avg_value
            row = [
                _escape_latex(language),
                _format_metric_value(avg_value, decimals=decimals),
                _format_metric_value(wc_value, decimals=decimals),
                _format_metric_value(delta_value, decimals=decimals),
                _format_metric_value(robustness_value, decimals=decimals),
            ]
            lines.append(" & ".join(row) + r" \\")

    lines.extend(
        [
            r"\hline",
            r"\end{tabular}",
            r"\end{table}",
        ]
    )
    return "\n".join(lines)


def build_multilingual_avg_wc_by_language_table(
    avg_pivot: pd.DataFrame,
    wc_pivot: pd.DataFrame,
    caption: str,
    label: str,
    decimals: int = 1,
) -> str:
    avg_summary = _summarize_pivot_for_dimension(avg_pivot, "Language", LANGUAGE_ORDER)
    wc_summary = _summarize_pivot_for_dimension(wc_pivot, "Language", LANGUAGE_ORDER)
    delta_summary = wc_summary - avg_summary

    languages = [language for language in LANGUAGE_ORDER if language in avg_summary.columns]
    model_names = _ordered_models(avg_summary.index)

    headers_top = ["Language"]
    headers_bottom = [""]
    for model_name in model_names:
        headers_top.append(
            rf"\multicolumn{{3}}{{c}}{{\textbf{{{_escape_latex(_display_model_name(model_name))}}}}}"
        )
        headers_bottom.extend([r"$A_{avg}$", r"$A_{wst}$", r"$\Delta$"])

    col_spec = "l|" + "|".join("rrc" for _ in model_names)
    lines = [
        r"\begin{table}[h]",
        r"\centering",
        rf"\caption{{{caption}}}",
        rf"\label{{{label}}}",
        r"\resizebox{\textwidth}{!}{%",
        rf"\begin{{tabular}}{{{col_spec}}}",
        r"\hline",
        r"\textbf{Language} & " + " & ".join(headers_top[1:]) + r" \\",
        " & ".join(headers_bottom) + r" \\",
        r"\hline",
    ]

    for language in languages:
        row = [_escape_latex(language)]
        for model_name in model_names:
            row.append(_format_metric_value(avg_summary.loc[model_name, language], decimals=decimals))
            row.append(_format_metric_value(wc_summary.loc[model_name, language], decimals=decimals))
            row.append(_format_metric_value(delta_summary.loc[model_name, language], decimals=decimals))
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


def build_selected_model_perturbation_breakdown_table(
    eval_df: pd.DataFrame,
    perturbation_labels_df: pd.DataFrame,
    caption: str,
    label: str,
    decimals: int = 1,
) -> str:
    eval_df = _filter_eval_df_to_stem_subjects(eval_df)
    selected_models = [
        model_name
        for model_name in ROBUSTNESS_SUMMARY_MODELS
        if model_name in set(eval_df["Model"])
    ]
    if not selected_models:
        raise ValueError("None of the selected perturbation-breakdown models were found.")

    labeled_df = eval_df.merge(
        perturbation_labels_df,
        on=["Subject", "Problem_ID"],
        how="left",
    )
    missing_labels = labeled_df[labeled_df["Perturbation_Type"].isna()]
    if not missing_labels.empty:
        missing_templates = (
            missing_labels[["Subject", "Problem_ID"]]
            .drop_duplicates()
            .head(10)
            .to_dict("records")
        )
        raise ValueError(f"Missing perturbation labels for templates: {missing_templates}")

    lines = [
        r"\begin{table}[h]",
        r"\centering",
        rf"\caption{{{caption}}}",
        rf"\label{{{label}}}",
        r"\resizebox{\textwidth}{!}{%",
        r"\begin{tabular}{lrrrrrr}",
        r"\hline",
        (
            r"\textbf{Perturbation} & \textbf{Templates} & \textbf{Samples} & "
            r"\textbf{Correct} & \textbf{Error} & \textbf{Correct \%} & \textbf{Error \%} \\"
        ),
        r"\hline",
    ]

    for model_idx, model_name in enumerate(selected_models):
        if model_idx > 0:
            lines.append(r"\hline")
        lines.append(
            rf"\multicolumn{{7}}{{c}}{{\textit{{{_escape_latex(_display_model_name(model_name))}}}}} \\"
        )
        lines.append(r"\hline")
        model_df = labeled_df[labeled_df["Model"] == model_name]
        for perturbation_type in PERTURBATION_TYPE_ORDER:
            type_df = model_df[model_df["Perturbation_Type"] == perturbation_type]
            sample_count = len(type_df)
            template_count = (
                type_df[["Subject", "Problem_ID"]]
                .drop_duplicates()
                .shape[0]
            )
            correct_count = int(type_df["Accuracy"].sum())
            error_count = sample_count - correct_count
            correct_rate = correct_count / sample_count if sample_count else pd.NA
            error_rate = error_count / sample_count if sample_count else pd.NA
            row = [
                _escape_latex(PERTURBATION_TYPE_DISPLAY_NAMES[perturbation_type]),
                f"{template_count:,}",
                f"{sample_count:,}",
                f"{correct_count:,}",
                f"{error_count:,}",
                _format_metric_value(correct_rate, decimals=decimals),
                _format_metric_value(error_rate, decimals=decimals),
            ]
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

    eval_df = _filter_eval_df_to_stem_subjects(eval_df)
    total_questions = (
        eval_df[["Subject", "Problem_ID", "Instance"]]
        .drop_duplicates()
        .shape[0]
    )

    avg_metric_df = _compute_average_accuracy(eval_df)
    wc_metric_df = _compute_worst_case_accuracy(eval_df)

    metric_builders = {
        "average_case_accuracy": (
            avg_metric_df,
            r"Average-case accuracy ($\times 100$)",
        ),
        "worst_case_accuracy": (
            wc_metric_df,
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
            metric_description = ""
            overall_metric = "overall accuracy"
            metric_intro = f"{metric_title} on Sci-Rho with {total_questions:,} generated question instances."
            caption = (
                f"{metric_intro}{metric_description} "
                f'"ALL" denotes the {overall_metric}. The remaining columns report scores by '
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

    avg_pivot = _metric_df_to_subject_language_pivot(avg_metric_df)
    wc_pivot = _metric_df_to_subject_language_pivot(wc_metric_df)

    robustness_caption = (
        r"Selected-model multilingual robustness on Sci-Rho. "
        r"$A_{avg}$ and $A_{wst}$ denote average-case and worst-case accuracy ($\times 100$), "
        r"$\Delta=A_{wst}-A_{avg}$ ($\times 100$), and $\mathcal{R}=A_{wst}/A_{avg}$ ($\times 100$), "
        r"all averaged over subjects for each model-language pair."
    )
    robustness_latex = build_selected_model_language_robustness_table(
        avg_pivot=avg_pivot,
        wc_pivot=wc_pivot,
        caption=robustness_caption,
        label="tab:stem_vision_reasoning_robustness_language",
    )
    robustness_path = out_path / "stem_vision_reasoning_robustness_by_language.tex"
    robustness_path.write_text(robustness_latex + "\n", encoding="utf-8")
    saved_paths.append(robustness_path)

    multilingual_caption = (
        'Multilingual results on Sci-Rho. For each language, '
        r'$A_{avg}$ denotes average-case accuracy ($\times 100$), '
        r'$A_{wst}$ denotes worst-case accuracy ($\times 100$), and '
        r'$\Delta$ denotes the reduction $A_{wst} - A_{avg}$ ($\times 100$), '
        'all averaged over subjects.'
    )
    multilingual_latex = build_multilingual_avg_wc_by_language_table(
        avg_pivot=avg_pivot,
        wc_pivot=wc_pivot,
        caption=multilingual_caption,
        label="tab:stem_vision_multilingual_avg_wc_by_language",
    )
    multilingual_path = out_path / "stem_vision_multilingual_avg_wc_by_language.tex"
    multilingual_path.write_text(multilingual_latex + "\n", encoding="utf-8")
    saved_paths.append(multilingual_path)

    combined_caption = (
        'English-only results on Sci-Rho. For each subject, '
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

    perturbation_caption = (
        r"Perturbation-type breakdown on Sci-Rho for selected models. "
        r"Each row reports average-case correctness and error rates over the full set "
        r"of evaluated model-language-instance samples assigned to the perturbation type."
    )
    perturbation_latex = build_selected_model_perturbation_breakdown_table(
        eval_df=eval_df,
        perturbation_labels_df=_load_perturbation_labels(),
        caption=perturbation_caption,
        label="tab:stem_vision_perturbation_type_breakdown",
    )
    perturbation_path = out_path / "stem_vision_perturbation_type_breakdown_selected_models.tex"
    perturbation_path.write_text(perturbation_latex + "\n", encoding="utf-8")
    saved_paths.append(perturbation_path)

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
            metric_description = ""
            overall_metric = "overall accuracy"
            metric_intro = f"{metric_title} on Sci-Rho."
            caption = (
                f"{metric_intro}{metric_description} "
                f'"ALL" denotes the {overall_metric}. The remaining columns report scores by '
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

    robustness_caption = (
        r"Selected-model multilingual robustness on Sci-Rho. "
        r"$A_{avg}$ and $A_{wst}$ denote average-case and worst-case accuracy ($\times 100$), "
        r"$\Delta=A_{wst}-A_{avg}$ ($\times 100$), and $\mathcal{R}=A_{wst}/A_{avg}$ ($\times 100$), "
        r"all averaged over subjects for each model-language pair."
    )
    robustness_latex = build_selected_model_language_robustness_table(
        avg_pivot=avg_pivot,
        wc_pivot=wc_pivot,
        caption=robustness_caption,
        label="tab:stem_vision_reasoning_robustness_language",
    )
    robustness_path = out_path / "stem_vision_reasoning_robustness_by_language.tex"
    robustness_path.write_text(robustness_latex + "\n", encoding="utf-8")
    saved_paths.append(robustness_path)

    multilingual_caption = (
        'Multilingual results on Sci-Rho. For each language, '
        r'$A_{avg}$ denotes average-case accuracy ($\times 100$), '
        r'$A_{wst}$ denotes worst-case accuracy ($\times 100$), and '
        r'$\Delta$ denotes the reduction $A_{wst} - A_{avg}$ ($\times 100$), '
        'all averaged over subjects.'
    )
    multilingual_latex = build_multilingual_avg_wc_by_language_table(
        avg_pivot=avg_pivot,
        wc_pivot=wc_pivot,
        caption=multilingual_caption,
        label="tab:stem_vision_multilingual_avg_wc_by_language",
    )
    multilingual_path = out_path / "stem_vision_multilingual_avg_wc_by_language.tex"
    multilingual_path.write_text(multilingual_latex + "\n", encoding="utf-8")
    saved_paths.append(multilingual_path)

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
            r"\caption{English-only results on Sci-Rho. For each subject, "
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

    if EVAL_CACHE_PATH.exists():
        eval_df = pd.read_pickle(EVAL_CACHE_PATH)
        perturbation_caption = (
            r"Perturbation-type breakdown on Sci-Rho for selected models. "
            r"Each row reports average-case correctness and error rates over the full set "
            r"of evaluated model-language-instance samples assigned to the perturbation type."
        )
        perturbation_latex = build_selected_model_perturbation_breakdown_table(
            eval_df=eval_df,
            perturbation_labels_df=_load_perturbation_labels(),
            caption=perturbation_caption,
            label="tab:stem_vision_perturbation_type_breakdown",
        )
        perturbation_path = out_path / "stem_vision_perturbation_type_breakdown_selected_models.tex"
        perturbation_path.write_text(perturbation_latex + "\n", encoding="utf-8")
        saved_paths.append(perturbation_path)

    return saved_paths


def main() -> None:
    if EVAL_CACHE_PATH.exists():
        eval_df = pd.read_pickle(EVAL_CACHE_PATH)
        saved_paths = export_latex_tables(eval_df, DEFAULT_LATEX_OUT_DIR)
    else:
        saved_paths = export_latex_tables_from_metric_files()
    for path in saved_paths:
        print(path)


if __name__ == "__main__":
    main()
