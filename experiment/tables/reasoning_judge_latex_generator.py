from __future__ import annotations

import argparse
from pathlib import Path
import re

import pandas as pd


EXPERIMENT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SUMMARY_PATH = EXPERIMENT_ROOT / "reasoning_judge" / "output" / "reasoning_judge_summary.xlsx"
DEFAULT_OUTPUT_PATH = EXPERIMENT_ROOT / "result" / "tables" / "latex" / "reasoning_judge_subject_metrics.tex"

DEFAULT_MODELS = [
    "gpt-5_4-2026-03-05",
    "OpenGVLab_InternVL3_5-8B",
    "Qwen_Qwen3-VL-8B-Instruct",
    "allenai_Molmo2-8B",
    "google_gemma-3-4b-it",
]

MODEL_DISPLAY_NAMES = {
    "gpt-5_4-2026-03-05": "GPT-5.4",
    "OpenGVLab_InternVL3_5-8B": "InternVL3.5-8B",
    "Qwen_Qwen3-VL-8B-Instruct": "Qwen3-VL-8B",
    "allenai_Molmo2-8B": "Molmo2-8B",
    "google_gemma-3-4b-it": "Gemma-3-4B-IT",
}

SUBJECT_ORDER = [
    "mathematics",
    "physics",
    "chemistry",
    "biology",
    "compsci",
]

SUBJECT_DISPLAY_NAMES = {
    "mathematics": "Math",
    "physics": "Phys",
    "chemistry": "Chem",
    "biology": "Bio",
    "compsci": "CS",
}

METRICS = [
    ("precision_mean", r"$\mathcal{P}$"),
    ("recall_mean", r"$\mathcal{R}$"),
    ("f1_mean", r"$\mathcal{F}$"),
    ("worst_case_f1_mean", r"$\mathcal{F}_{wst}$"),
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


def _format_metric_value(value: object, decimals: int = 1) -> str:
    if pd.isna(value):
        return "-"
    return f"{float(value) * 100:.{decimals}f}"


def _load_summary(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Missing summary file: {path}")
    df = pd.read_excel(path)
    required_columns = {"model", "subject", "precision_mean", "recall_mean", "worst_case_f1_mean"}
    missing_columns = required_columns.difference(df.columns)
    if missing_columns:
        raise ValueError(f"Summary file is missing columns: {sorted(missing_columns)}")
    df["model"] = df["model"].astype(str)
    df["subject"] = df["subject"].astype(str).str.lower()
    return df


def build_reasoning_judge_table(
    summary_df: pd.DataFrame,
    models: list[str],
    decimals: int = 1,
    caption: str | None = None,
    label: str = "tab:reasoning_judge_subject_metrics",
) -> str:
    resolved_caption = caption or r"Reasoning-judge subject-level results ($\times 100$). Missing results are shown as -."
    model_group_spec = "|".join(["rrrr"] * len(models))
    col_spec = "l|" + model_group_spec
    lines = [
        r"\begin{table}[h]",
        r"\centering",
        rf"\caption{{{resolved_caption}}}",
        rf"\label{{{label}}}",
        r"\resizebox{\textwidth}{!}{%",
        rf"\begin{{tabular}}{{{col_spec}}}",
        r"\hline",
        " & ".join(
            [r"\textbf{Subject}"]
            + [rf"\multicolumn{{4}}{{c}}{{\textbf{{{_escape_latex(MODEL_DISPLAY_NAMES.get(model, model))}}}}}" for model in models]
        ) + r" \\",
        " & ".join(
            [""]
            + [rf"\textbf{{{metric_label}}}" for _ in models for _, metric_label in METRICS]
        ) + r" \\",
        r"\hline",
    ]

    indexed = summary_df.set_index(["subject", "model"])
    for subject in SUBJECT_ORDER:
        subject_label = _escape_latex(SUBJECT_DISPLAY_NAMES.get(subject, subject.title()))
        values: list[str] = []
        for model in models:
            for metric_column, _ in METRICS:
                if (subject, model) not in indexed.index:
                    values.append("-")
                    continue
                value = indexed.loc[(subject, model), metric_column]
                if isinstance(value, pd.Series):
                    value = value.iloc[0]
                values.append(_format_metric_value(value, decimals=decimals))
        lines.append(" & ".join([subject_label, *values]) + r" \\")
    lines.append(r"\hline")

    lines.extend(
        [
            r"\end{tabular}%",
            r"}",
            r"\end{table}",
        ]
    )
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a LaTeX table for reasoning-judge subject metrics."
    )
    parser.add_argument(
        "--summary-path",
        type=Path,
        default=DEFAULT_SUMMARY_PATH,
        help="Path to reasoning_judge_summary.xlsx",
    )
    parser.add_argument(
        "--output-path",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="Where to write the generated .tex table",
    )
    parser.add_argument(
        "--model",
        dest="models",
        action="append",
        help="Model id to include as a column. Repeat to override the default 5-model set.",
    )
    parser.add_argument(
        "--decimals",
        type=int,
        default=1,
        help="Number of decimals to show after scaling scores by 100.",
    )
    parser.add_argument(
        "--caption",
        default=None,
        help="Optional custom LaTeX caption.",
    )
    parser.add_argument(
        "--label",
        default="tab:reasoning_judge_subject_metrics",
        help="LaTeX label for the table.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    models = args.models if args.models else DEFAULT_MODELS
    summary_df = _load_summary(args.summary_path)
    latex = build_reasoning_judge_table(
        summary_df=summary_df,
        models=models,
        decimals=args.decimals,
        caption=args.caption,
        label=args.label,
    )
    args.output_path.parent.mkdir(parents=True, exist_ok=True)
    args.output_path.write_text(latex, encoding="utf-8")
    print(args.output_path)


if __name__ == "__main__":
    main()
