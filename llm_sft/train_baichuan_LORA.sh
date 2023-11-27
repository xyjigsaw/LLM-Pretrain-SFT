# pip3 install -r requirements.txt

BASE_MODEL_PATH=/home/reacubeth/models/baichuan-2-7b-base-pretrain
EPOCH=10

TITLE=baichuan-2-7b-base-pretrain-lr1e5epoch5data12length512-LORA
DATA=data

OUTPUT_DIR=result

echo ===== current OUTPUT_DIR is $OUTPUT_DIR =====

torchrun --nproc_per_node=4 --master_port=2219 train_lora.py \
    --model_name_or_path $BASE_MODEL_PATH \
    --data_path $DATA \
    --bf16 True \
    --output_dir $OUTPUT_DIR \
    --num_train_epochs $EPOCH \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 1 \
    --evaluation_strategy "no" \
    --save_strategy "epoch" \
    --save_steps 1000 \
    --save_total_limit 1 \
    --learning_rate 2e-5 \
    --weight_decay 0. \
    --logging_steps 1 \
    #--deepspeed "./configs/default_offload_opt_param.json" \
    #--tf32 True \
    #--use_lora True \
