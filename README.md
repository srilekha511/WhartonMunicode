# WhartonMunicode
A repository built off of [Andrej Karpathy's nanoGPT](https://github.com/karpathy/nanoGPT): a smaller scale version of ChatGPT able to run on your personal computer. 

This repository is part of a project at the Wharton School of the University of Pennsylvania aiming to adopt large language models (LLMs) - such as ChatGPT - for use in the legal space. It aims to lay foundational work for future implementation in this area. 

Want to learn more about the computational theory behind LLMs, and how they can potentially advance the legal space? [look no further](https://docs.google.com/presentation/d/1TlQq6ndbHNnc1HoaDdSs_5NzbDtv8IifhZzLYyMxuos/edit?usp=sharing).

WhartonMunicode is designed, as the name suggests, to accept municipal codes as input. Input text to train the nanoGPT model was taken from [municode](https://library.municode.com/), a library containing over 3300 municipal codes for towns across the country. Below are beginner-friendly instructions for setting up and training the model on your own device. 

# Setup

These setup instructions are compatible for setting up and running this repository with Google Colab. However, these instructions nearly remain the same for setup in Jupyter Notebook or any other platform. 

First, mount Google Drive onto the Colab interface. This is necessary to facilitate the cloning of the repository. If you are working on Jupyter Notebook or any other platform, skip this step (Jupyter is based on the local files of your computer, not a cloud platform)

```
from google.colab import drive
drive.mount('/content/drive')
```

# Packages in Use

This repository implements the same packages as nanoGPT:

- [transformers](https://pypi.org/project/transformers/): HuggingFace package, contains pretrained models to perform tasks on text, vision, and audio
- [datasets](https://pypi.org/project/datasets/): HuggingFace package, allows for more efficient data pre-processing
- [tiktoken](https://github.com/openai/tiktoken): OpenAI's BPE tokenizer, takes in data and separates it into tokens for training
- [tqdm](https://tqdm.github.io/): Python package for progress bars
- [wandb](https://wandb.ai/site): "Weights and Biases", primarily used to track metrics such as accuracy and loss during model training and evaluation
- [numpy](https://numpy.org/): Essential Python library to operate on datasets in multidimensional array or matrix form
- [httpx](https://www.python-httpx.org/): Python web client package used to get data from websites
- [torch](https://pytorch.org/): Python library using the PyTorch framework, used for various machine learning applications from NLP to computer vision to deep learning models.

  ## Using these Packages

  Next, import these packages. This may take a few seconds to a minute or two depending on if these packages have been imported before, as well as the computing speed and power of your computer.

  ```
  pip install transformers datasets tiktoken tqdm wandb numpy httpx torch
  ```

# Working With WhartonMunicode

## Cloning Repository

If you are in Google Colab:

Clone this repository to get a local copy in the platform of your choice. (Google Colab users will find the repository in the "Files" tab on the left hand vertical bar, while Jupyter Notebook users will find that the repository clones into the same folder path of the notebook)

```
!git clone https://github.com/srilekha511/Wharton_Municode
```

If you are in Jupyter Notebook:

Cloning a Github repository must be done through the terminal. Navigate to the folder containing the .ipynb notebook. Click on the "New" dropdown menu on the upper right hand side and select "Terminal". In the terminal window, type:

```
git clone https://github.com/srilekha511/Wharton_Municode
```

WhartonMunicode will clone into the folder and will be visible upon refreshing the Jupyter Notebook interface. 

## Running prepare.py

If you are in Google Colab:

First change directories into the the municodes folder of this repository. Colab won't let you run files unless you are in the exact folder path containing it. Then, run the script `prepare.py`:
```
%cd /content/Wharton_Municode/data/municode
!python prepare.py
```

Your output should return the file path of the `train.bin` and the `val.bin`, which should most likely be `/content/Wharton_Municode/data/municode`. The `train.bin` and `val.bin` files store the tokens of the training and validation files, respectively (`tiktoken` was used to tokenize the text to prepare it for training). 
The output should also print the number of training and validation tokens there are. For example, if we loaded in the municipal code for the city of Alvarado, Texas (the default dataset in this repository), it should print

```
train has 585,895 tokens
val has 64,881 tokens
```
The larger the number of tokens, the more data the machine learning algorithm can work with to make predictions. See `prepare.py` for a more in-depth explanation. 

## Training prepare.py

If you are in Google Colab:

The `train.py` file is not in the data folder, so change directories out of it. Next, run `train.py` with the following settings:

```
%cd /content/Wharton_Municode
!python train.py config/train_municode_char.py --device=cpu --compile=False --eval_iters=20 --log_interval=1 --block_size=64 --batch_size=12 --n_layer=4 --n_head=4 --n_embd=128 --max_iters=2000 --lr_decay_iters=2000 --dropout=0.0
```
The `device` parameter can be changed to either a `cpu` or `gpu`, depending on the type of computer you have. 

If all goes well, the output should print each iteration of training along with the respective loss and time taken. The loss should progressively decrease as the number of iterations becomes greater. The parameter `lr_decay_iters` defines the number of iterations before `train.py` stops running and is currently set to 2000. On a CPU such as a MacBook, this can take at least 10-20 minutes, while a GPU can complete it in about idk minutes. 

## Viewing sample.py

Now that the model is trained, we can see view the language generation that mimics that of the original dataset:

```
!python sample.py --out_dir=out-municode-char --device=cpu
```
As before, change the `device` parameter to `cpu` or `gpu` as necessary. 

`sample.py` should start to output language similar to the municipal codes that were inputted. Keep in mind that WhartonMunicode is an elementary LLM and therefore its outputs have no semantical significance (yet). More advanced LLMs such as ChatGPT employ [supervised human labeling](https://openai.com/blog/chatgpt) to rank outputs to optimize outputs. 

Here is a short snippet of a sample output from training on the municipal code of Alvarado, TX:
```
                 It is prohibited by the terms of the inspector shall be maintained where the city ordinance or
               to Local Government Code ch.000 3)"
Sec. 2-20-64.,Prostandard residential police is required.,"(a)

                If an subdivider shall be required with the ground plan application, and such notice that the
               of this article.

               It shall be accompanied by the owner of the provisions and shall be it will be required by
                  has been paid to such street and for the state and other public and alley, the location of the
                  department, for proposed to review and the city engineer, that the plans shall
               Polaris or to the city council from the city.

               (b)

               The state fee shall be complied with the planning and land as a manner to prevent the
               such city and the health of public property regulations.

               (Code 2008, § 90.04)"
Sec. 8-130.,Definitions.,"The city, or his words, in itsNULL
                   .,General conditions in the city; premises by the operator or organization,
               and the police is the authority to the proposed for all such system on an immediate
               specific use or any ordinance
---------------

```
Notice that the output employs similar words, symbols, and language as that of the municipal code. Running WhartonMunicode on the same dataset will return different outputs each time. 
