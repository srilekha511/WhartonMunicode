# Municode

The prepare.py file begins by importing the input text file, either from a file path or from an external link. Training data is set to cover 90% of the text, while the validation set covers the remaining 10%. After the text file is loaded in and split, the tiktoken class is used to tokenize the data. Tokenization is essentially the splitting of the text into numerically converted chunks known as tokens. Large language models like ChatGPT function to predict the next "token", essentially predicting the next word fragment to eventually generate language.  

Run prepare.py to output the number of training and validation tokens. The number of tokens outputted depends on the size of the municipal code file. The IDs of the training and validation set tokens are exported to a bin file. 
