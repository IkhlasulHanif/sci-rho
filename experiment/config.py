from dataclasses import dataclass

@dataclass
#TODO: ADJUST (https://docs.vllm.ai/en/latest/api/vllm/#vllm.LLM)
class ModelConfig:
    dtype: str = "bfloat16"
    max_model_len: int = 2**14 # 16384
    tensor_parallel_size: int = 1 # (number of GPUs)
    gpu_memory_utilization: float = 0.95 # percentage of VRAM maximum utilization (beware OOM)
    swap_space: float = 4
    cpu_offload_gb: float = 0
    enforce_eager: bool = False

# TODO: ADJUST. PLEASE REFER TO (https://arxiv.org/pdf/2411.00836)
@dataclass
class SamplingConfig:
    max_tokens: int = 4096
    temperature: float = 0.0 # for deterministic result

@dataclass
class ExperimentConfig:
    model_names: tuple[str] = (
        "Qwen/Qwen3.5-9B",
        "meta-llama/Llama-3.2-11B-Vision-Instruct",
        "google/gemma-3-12b-it",
        "OpenGVLab/InternVL3_5-14B",
        "OpenGVLab/InternVL3_5-8B"
        "allenai/Molmo2-8B",
    )
    subject_list: tuple[str] = (
        "mathematics", 
        "physics", 
        "chemistry", 
        "biology", 
        "compsci"
    )
    debug: bool = False
    num_of_instance: int = 10 #TODO: ADJUST