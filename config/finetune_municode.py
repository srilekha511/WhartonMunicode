import time

out_dir = 'out-municode'
eval_interval = 5
eval_iters = 40
wandb_log = False # feel free to turn on
wandb_project = 'municode'
wandb_run_name = 'ft-' + str(time.time())

dataset = 'municode'
init_from = 'gpt2-xl' # this is the largest GPT-2 model

# only save checkpoints if the validation loss improves
always_save_checkpoint = False

batch_size = 1
gradient_accumulation_steps = 32
max_iters = 20

# finetune at constant LR
learning_rate = 3e-5
decay_lr = False
