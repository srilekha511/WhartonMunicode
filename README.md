# Wharton_Municode
A repository built off of [Andrej Karpathy's nanoGPT](https://github.com/karpathy/nanoGPT): a smaller scale version of ChatGPT able to run on your personal computer. 

This repository is part of a project at the Wharton School of the University of Pennsylvania aiming to adopt large language models - such as ChatGPT - for use in the legal space. It aims to lay foundational work for future implementation in this area. 

Wharton_Municode is designed, as the name suggests, to accept municipal codes as input. Input text to train the nanoGPT model was taken from [municode](https://library.municode.com/), a library containing over 3300 municipal codes for towns across the country. Below are beginner-friendly instructions for setting up and training the model on your own device. 

# Setup

These setup instructions are compatible for setting up and running this repository with Google Colab. However, these instructions nearly remain the same for setup in Jupyter Notebook or any other platform. 

First, mount Google Drive onto the Colab interface. This is necessary to facilitate the cloning of the repository. 

```
from google.colab import drive
drive.mount('/content/drive')
```


