import os
import torch
import json
from transformers import AutoModelForCausalLM, AutoTokenizer, TextGenerationPipeline
from transformers.generation.utils import GenerationConfig


PROMPT_DICT_ALPACA = {
    "prompt_input": (
        "Below is an instruction that describes a task, paired with an input that provides further context. "
        "Write a response that appropriately completes the request.\n\n"
        "### Instruction:\n{instruction}\n\n### Input:\n{input}\n\n### Response:"
    ),
    "prompt_no_input": (
        "Below is an instruction that describes a task. "
        "Write a response that appropriately completes the request.\n\n"
        "### Instruction:\n{instruction}\n\n### Response:"
    ),
}


if __name__ == '__main__':
    
    model_path = '/home/reacubeth/models/baichuan-2-7b-base/ckpt/baichuan-2-7b-base-pretrain'

    GPU_ID = 0
    os.environ["CUDA_VISIBLE_DEVICES"] = str(GPU_ID)
    os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"


    if torch.cuda.is_available():
        device = 0
    else:
        raise ValueError("No GPU available")
        device = -1

    if 'baichuan' in model_path:
        if 'lora' in model_path.lower():
            print('using lora model')
            from peft import AutoPeftModelForCausalLM
            model = AutoPeftModelForCausalLM.from_pretrained(model_path, trust_remote_code=True)
            tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=True, trust_remote_code=True)
        else:
            tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=True, trust_remote_code=True)
            model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto", trust_remote_code=True)
    else:
        model = AutoModelForCausalLM.from_pretrained(model_path)
        tokenizer = AutoTokenizer.from_pretrained(model_path)

    generator = TextGenerationPipeline(model=model, tokenizer=tokenizer, device=device)

    prompt_no_input = PROMPT_DICT_ALPACA["prompt_no_input"]

    while True:
        print('-' * 100)
        user_input = ''
        while True:
            cur_input = input('# user: ')
            if cur_input == 'q':
                break
            user_input += cur_input
            user_input += '\n'
        prompt = {
            "instruction": user_input,
        }
        if 'mistral' in model_path.lower():
            outputs = generator([prompt_no_input.format_map(prompt)], max_new_tokens=200, num_beams=4, pad_token_id=tokenizer.eos_token_id)
        else:
            outputs = generator([prompt_no_input.format_map(prompt)], max_new_tokens=200, num_beams=4)
        print('# bot: \n', outputs[0][0]['generated_text'][len(prompt_no_input.format_map(prompt)):].strip())

