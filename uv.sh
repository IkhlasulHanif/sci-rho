#!/usr/bin/env bash

set -euo pipefail

packages=(
  
  numpy
  pandas
  matplotlib
  scipy
  pillow
  networkx
  sympy
  matplotlib-venn
  openpyxl
  requests
  tqdm
  huggingface-hub
  anthropic
  openai
  google-genai
  torch
  torchvision
  transformers
  vllm
)

for package in "${packages[@]}"; do
  echo "==> uv add ${package}"
  uv add "${package}"
done

echo "==> uv add --frozen vllm"
uv add --frozen vllm
