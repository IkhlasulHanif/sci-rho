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
        "Qwen/Qwen3.5-9B",
        "meta-llama/Llama-3.2-11B-Vision-Instruct",
        "google/gemma-3-12b-it",
        "allenai/Molmo2-8B",
        "OpenGVLab/InternVL3_5-14B",
        "OpenGVLab/InternVL3_5-8B"
    )
    subject_list: tuple[str] = (
        "mathematics", 
        "physics", 
        "chemistry", 
        "biology", 
        "compsci"
    )
    debug: bool = False
    num_of_instance: int = 5