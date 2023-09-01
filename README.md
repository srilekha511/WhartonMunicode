# Wharton_Municode
A repository built off of [Andrej Karpathy's nanoGPT](https://github.com/karpathy/nanoGPT): a smaller scale version of ChatGPT able to run on your personal computer. 

This repository is part of a project at the Wharton School of the University of Pennsylvania aiming to adopt large language models - such as ChatGPT - for use in the legal space. It aims to lay foundational work for future implementation in this area. 

Wharton_Municode is designed, as the name suggests, to accept municipal codes as input. Input text to train the nanoGPT model was taken from [municode](https://library.municode.com/), a library containing over 3300 municipal codes for towns across the country. Below are beginner-friendly instructions for setting up and training the model on your own device. 

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

  Next, import these packages. This may take a few seconds to a minute depending on if these packages have been imported before, as well as the computing speed and power of your computer.

  ```
  pip install transformers datasets tiktoken tqdm wandb numpy httpx torch
  ```

