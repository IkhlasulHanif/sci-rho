import os
import json
import pandas as pd
import PIL
import gc
import torch
from dataclasses import fields, asdict

from vllm import LLM, SamplingParams
from transformers import AutoTokenizer
from argparse import ArgumentParser
from dataclasses import fields
from config import *
from huggingface_hub import login

def add_args_from_dataclass(parser, dc, prefix=""):
    for f in fields(dc):
        arg_name = f"--{prefix}{f.name}"
        parser.add_argument(arg_name, default=f.default, type=f.type)

def extract_config(args, cls, prefix):
    kwargs = {f.name: getattr(args, f"{prefix}{f.name}") for f in fields(cls)}
    return cls(**kwargs)


def main():
    hf_token = os.environ.get("HF_TOKEN")
    if hf_token:
        login(token=hf_token)
        print("Hugging Face login succeeded.")
    else:
        print("HF_TOKEN is not set.")
        
    parser = ArgumentParser()
    add_args_from_dataclass(parser, ModelConfig, prefix="model.")
    add_args_from_dataclass(parser, SamplingConfig, prefix="sampling.")
    add_args_from_dataclass(parser, ExperimentConfig, prefix="experiment.")
    args = parser.parse_args()

    model_cfg = extract_config(args, ModelConfig, "model.")
    sampling_cfg = extract_config(args, SamplingConfig, "sampling.")
    experiment_cfg = extract_config(args, ExperimentConfig, "experiment.")

    NUM_OF_INSTANCES = 1 if experiment_cfg.debug else experiment_cfg.num_of_instance

    user_prompt_path = "user_prompt.txt"
    if not os.path.exists(user_prompt_path):
        raise FileNotFoundError(f"User prompt template not found at {user_prompt_path}. Terminating execution.")

    with open(user_prompt_path, "r", encoding="utf-8") as f:
        user_prompt_template = f.read().strip()
    print(f"[INFO] Successfully loaded additional prompt template from {user_prompt_path}")

    for model_name in experiment_cfg.model_names:
        print(f"\n{'='*60}\n[INFO] LOADING MODEL: {model_name}\n{'='*60}")
        llm = LLM(model=model_name, **asdict(model_cfg))
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        for subject in experiment_cfg.subject_list:
            print(f"\n[INFO] Starting Subject: {subject.upper()}")

            for index in range(NUM_OF_INSTANCES):
                print(f"[INFO]   -> Processing Instance: 0{index}")

                dataset_path = os.path.join("sample", f"0{index}", subject)
                json_path = os.path.join(dataset_path, 'dataset.json')

                if not os.path.exists(json_path):
                    raise FileNotFoundError(f"Dataset JSON not found at {json_path}. Terminating execution.")

                with open(json_path, 'r') as file:
                    data = json.load(file)
                df = pd.DataFrame.from_dict(data, orient="index")

                if len(df) == 0:
                    raise ValueError(f"Instance 0{index} for {subject} has no data. Terminating execution.")

                df.insert(0, "id", range(1, len(df) + 1))
                desc_columns = [col for col in df.columns if col.startswith("description")]
                df_new = df.copy()

                for desc_col in desc_columns:
                    variant_name = desc_col.replace("description_", "") if desc_col != "description" else "default (English)"
                    print(f"[INFO]      --> Generating Model: {model_name} | Variant: {variant_name.upper()} | Column: {desc_col}")

                    messages = [
                        [{"role": "user", "content": [
                            {"type": "image"},
                            {"type": "text", "text": f"{desc}\n\n{user_prompt_template}" if user_prompt_template else desc},
                        ]}]
                        for desc in df[desc_col]
                    ]

                    sampling_params = SamplingParams(**asdict(sampling_cfg))
                    prompts = tokenizer.apply_chat_template(messages, tokenize=False)

                    requests = [
                        {
                            "prompt": p,
                            "multi_modal_data": {"image": PIL.Image.open(os.path.join(dataset_path, img.replace("\\", os.sep)))}
                        }
                        for p, img in zip(prompts, df["image"])
                    ]

                    outputs = llm.generate(requests, sampling_params)
                    responses = [o.outputs[0].text for o in outputs]

                    result_col_name = desc_col.replace("description", "response")
                    df_new[result_col_name] = responses

                output_filename = f'{model_name}'.replace("/", "_").replace(".", "_") + '.xlsx'
                output_path = os.path.join('result', 'raw', subject, f"0{index}")
                os.makedirs(output_path, exist_ok=True)
                full_output_path = os.path.join(output_path, output_filename)
                df_new.to_excel(full_output_path, index=False, engine="openpyxl")
                print(f"[INFO]   -> Saved results to {full_output_path}")

        print(f"\n[INFO] Unloading {model_name} and clearing VRAM...")
        del llm
        gc.collect()
        torch.cuda.empty_cache()
        print("[INFO] VRAM cleared successfully.")


if __name__ == '__main__':
    main()