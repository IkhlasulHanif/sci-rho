import os
import json
import pandas as pd
import PIL
import gc
import torch

from vllm import LLM, SamplingParams
from transformers import AutoTokenizer
from argparse import ArgumentParser
from dataclasses import fields
from config import *

# function to load args from config.py
def add_args_from_dataclass(parser, dc, prefix=""):
    for f in fields(dc):
        arg_name = f"--{prefix}{f.name}"
        parser.add_argument(
            arg_name,
            default=f.default,
            type=f.type,
        )

# function to extract config
def extract_config(args, cls, prefix):
    kwargs = {
        f.name: getattr(args, f"{prefix}{f.name}")
        for f in fields(cls)
    }
    return cls(**kwargs)

# load config.py
parser = ArgumentParser()
add_args_from_dataclass(parser, ModelConfig, prefix="model.")
add_args_from_dataclass(parser, SamplingConfig, prefix="sampling.")
add_args_from_dataclass(parser, ExperimentConfig, prefix="experiment.")
args = parser.parse_args()

# extract config
model_cfg = extract_config(args, ModelConfig, "model.")
sampling_cfg = extract_config(args, SamplingConfig, "sampling.")
experiment_cfg = extract_config(args, ExperimentConfig, "experiment.")

# process only one instance when debugging
if experiment_cfg.debug:
    NUM_OF_INSTANCES = 1
else:
    NUM_OF_INSTANCES = 10

# loop for all models, then all subjects, then all instances
for model_name in experiment_cfg.model_names:
    llm = LLM(
        model=model_name,
        dtype=model_cfg.dtype,
        max_model_len=model_cfg.max_model_len,
        tensor_parallel_size=model_cfg.tensor_parallel_size,
        gpu_memory_utilization=model_cfg.gpu_memory_utilization,
        swap_space=model_cfg.swap_space,
        cpu_offload_gb=model_cfg.cpu_offload_gb,
        enforce_eager=model_cfg.enforce_eager
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    for subject in experiment_cfg.subject_list:
        for index in range(NUM_OF_INSTANCES):

            # process dataset
            dataset_path = os.path.join("sample", f"0{index}", subject) # ex: 'sample/01/physics/'
            json_path = os.path.join(dataset_path, 'dataset.json') # ex: 'sample/01/physics/dataset.json'
            with open(json_path, 'r') as file:
                data = json.load(file)
            df = pd.DataFrame.from_dict(data, orient="index")
            if len(df) == 0: # skip if instance has no data. To be deleted later
                continue
            df.insert(0, "id", range(1, len(df) + 1)) # insert `id` starting from 1

            # process chat template
            messages = [
                [
                    {
                        "role": "user",
                        "content": [
                            {"type": "image"},
                            {"type": "text", "text": desc},
                        ],
                    }
                ]
                for desc in df["description"]
            ]
            sampling_params = SamplingParams(
                max_tokens=sampling_cfg.max_tokens,
                temperature=sampling_cfg.temperature
            )
            prompts = tokenizer.apply_chat_template(messages, tokenize=False)

            # make vLLM requests
            requests = [
                {
                    "prompt": desc,
                    "multi_modal_data": {"image": PIL.Image.open(os.path.join(dataset_path, img.replace("\\", os.sep)))}
                }
                for desc, img in zip(prompts, df["image"])
            ]

            # generate LLM responses
            outputs = llm.generate(requests)

            # extract responses
            responses = []
            for o in outputs:
                responses.append(o.outputs[0].text)
            
            # merge response with df
            df_new = df.copy()
            df_new[model_name] = responses

            # save df to .xlsx
            output_filename = f'{model_name}'.replace("/", "_").replace(".", "_") + '.xlsx'
            output_path = os.path.join('result', 'raw', subject, f"0{index}") # ex: 'result/raw/physics/00'
            os.makedirs(output_path, exist_ok=True)
            full_output_path = os.path.join(output_path, output_filename) # ex: 'result/raw/physics/00/model_name.xlsx'
            df_new.to_excel(full_output_path, index=False, engine="openpyxl")

    # clear memory
    del llm
    gc.collect()
    torch.cuda.empty_cache()