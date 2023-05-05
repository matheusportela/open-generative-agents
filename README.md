# Open Generative Agents

An open-source implementation of [Generative Agents](https://arxiv.org/abs/2304.03442) (Park et al., 2023).

## Install
```bash
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Installing LLM
You can use [llama.cpp](https://github.com/ggerganov/llama.cpp) with [OpenLLaMA](https://github.com/openlm-research/open_llama) weights.

```bash
# Install prerequisites
brew install cmake git-lfs && git lfs install

# Install llama.cpp
git clone https://github.com/ggerganov/llama.cpp && cd llama.cpp && cmake -B build && cmake --build build
virtualenv venv_llama && source venv_llama/bin/activate
python -m pip install -r requirements.txt

# Download OpenLLaMA weights
cd models && git clone https://huggingface.co/openlm-research/open_llama_7b_preview_300bt/ && cd ..
python convert-pth-to-ggml.py models/open_llama_7b_preview_300bt/open_llama_7b_preview_300bt_transformers_weights 1
./build/bin/quantize models/open_llama_7b_preview_300bt/open_llama_7b_preview_300bt_transformers_weights/ggml-model-f16.bin models/open_llama_7b_preview_300bt_q5_0.ggml q5_0

# Test LLM
./build/bin/main -m models/open_llama_7b_preview_300bt_q5_0.ggml -n 1280 -p "Building a website can be done in 3 simple steps:" --mlock
```

## Run
```bash
python generative_agents.py
```

## Test
```bash
mypy engine
pytest
```
