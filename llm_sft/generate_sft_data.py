#    Copyright 2023 Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import copy
import logging
import json
import random
import os
from dataclasses import dataclass, field
from typing import Dict, Optional, Sequence

import torch
import transformers
import utils
from torch.utils.data import Dataset

IGNORE_INDEX = -100
DEFAULT_PAD_TOKEN = "[PAD]"
DEFAULT_EOS_TOKEN = "</s>"
DEFAULT_BOS_TOKEN = "<s>"
DEFAULT_UNK_TOKEN = "<unk>"


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


class RawSupervisedDataset(Dataset):
    """Raw Dataset for supervised fine-tuning."""

    def __init__(self, data_path: str, tokenizer: transformers.PreTrainedTokenizer):
        super(RawSupervisedDataset, self).__init__()
        logging.warning("Loading data...")
        prompt_no_input = PROMPT_DICT_ALPACA["prompt_no_input"]
        prompt_input = PROMPT_DICT_ALPACA["prompt_input"]
        print('prompt_no_input: ', prompt_no_input)

        multi_tasks_source_data = []
        multi_tasks_target_data = []

        for file in os.listdir(data_path):
            if file.endswith(".json") and 'alpaca' not in file:
                cur_data_path = data_path + '/' + file
                print('-'*80)
                print('cur_data_path: ', cur_data_path)
                logging.warning('cur_data_path: ' + cur_data_path)
                with open(cur_data_path, "r") as f:
                    sft_data = json.load(f)
                for task in sft_data:
                    print('Task name: ', task, ' length: ', len(sft_data[task]))
                    logging.warning('Task name: ' + task + ' length: ' + str(len(sft_data[task])))
                    for item in sft_data[task]:
                        multi_tasks_source_data.append(prompt_no_input.format_map(item))
                        multi_tasks_target_data.append(f"{item['output']}{tokenizer.eos_token}")
        print('multi_tasks_source_data length: ', len(multi_tasks_source_data))
        logging.warning("multi_tasks_source_data length: " + str(len(multi_tasks_source_data)))

        # load alpaca data
        alpaca_data = utils.jload(data_path + '/alpaca_data.json')
        source_alpaca_data = [prompt_input.format_map(item) if item.get("input", "") != "" else prompt_no_input.format_map(item) for item in alpaca_data]
        target_alpaca_data = [f"{item['output']}{tokenizer.eos_token}" for item in alpaca_data]
        print('alpaca_data length: ', len(source_alpaca_data))
        logging.warning("alpaca_data length: " + str(len(source_alpaca_data)))

        logging.warning("Loading data finished.")

        source_all = multi_tasks_source_data + source_alpaca_data
        target_all = multi_tasks_target_data + target_alpaca_data

        # shuffle data
        random_index = random.sample(range(len(source_all)), len(source_all))
        self.source_all = [source_all[i] for i in random_index]
        self.target_all = [target_all[i] for i in random_index]

        print('source_all length: ', len(source_all))
        logging.warning("source_all length: " + str(len(source_all)))


# main
if __name__ == "__main__":
    raw_dataset = RawSupervisedDataset(data_path='data', tokenizer=transformers.GPT2Tokenizer.from_pretrained('gpt2'))
