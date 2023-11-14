# pip3 install -r requirements.txt

BASE_MODEL_PATH=/home/reacubeth/models/llama-7b-pretrain/

EPOCH=3
TITLE=llama-7b-pretrain-lr1e5epoch5data12length512
DATA=data

OUTPUT_DIR=result

echo ===== current OUTPUT_DIR is $OUTPUT_DIR =====

torchrun --nproc_per_node=4 --master_port=9919 train.py \
    --model_name_or_path $BASE_MODEL_PATH \
    --data_path $DATA \
    --bf16 True \
    --output_dir $OUTPUT_DIR \
    --num_train_epochs $EPOCH \
    --per_device_train_batch_size 4 \
    --per_device_eval_batch_size 4 \
    --gradient_accumulation_steps 8 \
    --evaluation_strategy "no" \
    --save_strategy "epoch" \
    --save_steps 1000 \
    --save_total_limit 1 \
    --learning_rate 2e-5 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --fsdp "full_shard auto_wrap" \
    --fsdp_transformer_layer_cls_to_wrap 'LlamaDecoderLayer' \
    --tf32 True \

