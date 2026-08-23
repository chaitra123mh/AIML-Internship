# W7D4: LlamaIndex + Ollama — Local RAG

## Objective

Build and test a local LLM inference workflow using Ollama and compare
llama3.2:3b with qwen2.5:3b.

## Models Used

- llama3.2:3b
- qwen2.5:3b
- nomic-embed-text

## Task 1: Ollama Setup

Ollama was already installed and the required models were available locally.

Verified models:

- llama3.2:3b
- qwen2.5:3b
- nomic-embed-text

## Task 2: Custom System Prompt

A Python script was created using the Ollama Python API.

File:

`ollama_inference.py`

The script uses a custom AI/ML mentor system prompt and tests 5 prompts.

All 5 prompts completed successfully.

Output:

`outputs/ollama_5_prompts.txt`

## Task 3: Model Comparison

The same 3 questions were tested using:

- llama3.2:3b
- qwen2.5:3b

File:

`model_comparison.py`

The comparison considers:

- Answer quality
- Clarity
- Level of detail
- Response latency

Output:

`outputs/model_comparison.txt`

## Conclusion

Both local models successfully generated responses for the same questions.
The comparison was performed using identical prompts so that their response
quality and latency could be evaluated consistently.

## Evidence

Screenshots of the 5-prompt inference and model comparison are stored in:

`Screenshots/`

## Self-Review

- [x] Ollama installed
- [x] llama3.2:3b verified
- [x] qwen2.5:3b verified
- [x] Custom system prompt implemented
- [x] 5 prompts tested
- [x] Same 3 questions tested on both models
- [x] Response quality compared
- [x] Output evidence saved
- [ ] CIA Mentor Mode interaction 1
- [ ] CIA Mentor Mode interaction 2
- [ ] Git commits completed
- [ ] Branch pushed
- [ ] Pull Request created