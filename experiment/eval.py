import os
import json
import pandas as pd
import PIL

from vllm import LLM, SamplingParams
from transformers import AutoTokenizer

model_names = [
    'HuggingFaceTB/SmolVLM-256M-Instruct'
    # 'Qwen/Qwen3-VL-2B-Instruct'
    # "HuggingFaceTB/SmolVLM-500M-Instruct"
]

subjects = ["mathematics", "physics", "chemistry", "biology", "compsci"]

NUM_OF_INSTANCES = 10

# loop for all models, then all subjects, then all instances
for model_name in model_names:
    llm = LLM(model=model_name,
            dtype='float16',
            gpu_memory_utilization=0.7,
            max_model_len=2048,
            swap_space=8)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    for subject in subjects:
        for index in range(NUM_OF_INSTANCES):

            # process dataset
            dataset_path = os.path.join("sample", f"0{index}", subject) # ex: 'sample/01/physics/'
            json_path = os.path.join(dataset_path, 'dataset.json') # ex: 'sample/01/physics/dataset.json'
            with open(json_path, 'r') as file:
                data = json.load(file)
            df = pd.DataFrame.from_dict(data, orient="index")
            if len(df) == 0:
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
            sampling_params = SamplingParams(max_tokens=128)
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