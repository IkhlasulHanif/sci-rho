from dataclasses import dataclass

class ModelConfig:
    dtype: str = "bfloat16"
    max_model_len: int = 2**16
    tensor_parallel_size: int = 1
    gpu_memory_utilization: float = 0.9
    swap_space: float = 4
    cpu_offload_gb: float = 0
    enforce_eager: bool = False

@dataclass
class SamplingConfig:
    max_tokens: int = 2**15
    temperature: float = 0.0 # for deterministic result

@dataclass
class ExperimentConfig:
    model_names: tuple[str] = (
        "meta-llama/Llama-3.2-11B-Vision-Instruct",
        "meta-llama/Llama-4-Maverick-17B-128E-Instruct",
        "Qwen/Qwen3-VL-8B-Thinking",
        "Qwen/Qwen3-VL-30B-A3B-Thinking",
        "Skywork/Skywork-R1V3-38B",
        "Skywork/R1V4",
        "OpenGVLab/InternVL3_5-8B-HF",
        "OpenGVLab/InternVL3_5-38B-HF",
        "google/gemma-3-4b-it",
        "google/gemma-3-12b-it",
        "google/gemma-3-27b-it",
        "deepseek-ai/deepseek-vl2",
        "llava-hf/llava-v1.6-vicuna-7b-hf",
        "llava-hf/llava-v1.6-vicuna-13b-hf",
        "microsoft/Phi-4-multimodal-instruct"
    )
    subject_list: tuple[str] = (
        "mathematics", 
        "physics", 
        "chemistry", 
        "biology", 
        "compsci"
    )
    debug: bool = False