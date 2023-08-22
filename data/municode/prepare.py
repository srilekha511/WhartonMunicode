import os
import requests
import tiktoken
import numpy as np

data_url = 'https://github.com/srilekha511/municode_files/blob/main/AlvaradoTXComplete.txt'
response = requests.get(data_url)

if response.status_code == 200:
    content = response.text
else:
    print("Failed to download data.")
    content = None

if content is not None:
    n = len(content)
    train_data = content[:int(n * 0.9)]
    val_data = content[int(n * 0.9):]

# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")
train_ids = enc.encode_ordinary(train_data)
val_ids = enc.encode_ordinary(val_data)
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export training and validation token ids to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))
