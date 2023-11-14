# LLM-Pretrain-SFT
Scripts of LLM pretraining and finetuing (SFT)

**LoRA supported**

The repository is based on [tatsu-lab/stanford_alpaca](https://github.com/tatsu-lab/stanford_alpaca).

## Supported LLM

- [LLaMA 1 & 2](https://huggingface.co/meta-llama)
- [Baichuan 2](https://huggingface.co/baichuan-inc)
- [Mistral](https://huggingface.co/mistralai)

## Pretrain (Continual Pretrain)

1. Before you start continual pre-training LLM, you should provide the model name (huggingface) or local model path.

2. Prepare training data, you can use plain text in the format of **markdown or txt** for pretraining. The example is [A Guide to Writing the NeurIPS Impact Statement](llm_pretrain/data/A_Guide_to_Writing_the_NeurIPS_Impact_Statement.md). You can add more text corpus in the data folder.

3. Launch

```
pip install -r requirements.txt
cd llm_pretrain
./pretrain_llama.sh
```

Note that some parameter settings of these models are different.

## SFT

1. Before you start fine-tuning LLM, you should provide the model name (huggingface) or local model path.

2. Prepare training data, you can add your own task data like the example in [sft_examples.json](llm_sft/data/sft_examples.json), which is similar to the [alpaca_data.json](llm_sft/data/alpaca_data.json)

The format is as follows:

```
{
	"binary_selection": [
        {
            "instruction": "Does the following text violate the law?\nText: OH MY FUCKING GOD",
            "output": "No"
        },
        ...
    ],
    "another_task_name": [
        {
            "instruction": "How are you?",
            "output": "Not bad."
        },
        ...
    ],
    ...
}
```

Note that if you put the [alpaca_data.json](llm_sft/data/alpaca_data.json) in the data folder, the script will use it as part of the training data.

3. Launch

### Full Parameters

```
pip install -r requirements.txt
cd llm_sft
./train_llama.sh
```

### LoRA

```
pip install -r requirements.txt
cd llm_sft
./train_baichuan_LORA.sh
```

You can adjust the configurations in the [train_lora.py](llm_sft/train_lora.py). In our experiments, for baichuan, your transformers version should >= 4.29.0 and < 4.34.0.


Note that some parameter settings of these models are different.


## File Tree

```
.
├── LICENSE
├── README.md
├── llm_pretrain_clean
│   ├── data
│   │   └── A_Guide_to_Writing_the_NeurIPS_Impact_Statement.md
│   ├── evaluation
│   │   └── inference_single.py
│   ├── generate_pretrain_data.py
│   ├── pretrain.py
│   ├── pretrain_baichuan2.sh
│   ├── pretrain_llama.sh
│   ├── pretrain_mistral.sh
│   ├── requirementsX.txt
│   └── utils.py
└── sft_model_clean
    ├── README.md
    ├── configs
    │   └── default_offload_opt_param.json
    ├── data
    │   ├── alpaca_data.json
    │   └── sft_examples.json
    ├── evaluation
    │   └── inference_single.py
    ├── generate_sft_data.py
    ├── requirementsX.txt
    ├── train.py
    ├── train_baichuan.sh
    ├── train_baichuan_LORA.sh
    ├── train_llama.sh
    ├── train_lora.py
    ├── train_mistral.sh
    └── utils.py
```

