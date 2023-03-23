# Study on LSTM and its Applications
This repository contains a study on Long Short-Term Memory (LSTM) and its applications. LSTM is a type of Recurrent Neural Network (RNN) that is widely used in various applications such as speech recognition, natural language processing, and time series prediction.

# Theory

## Recurrent Neural Networks and the Vanishing Gradient Problem
Before we dive into LSTM networks, let's first discuss standard RNNs and the vanishing gradient problem they often face. RNNs are neural networks designed to work with sequential data, where the output from the previous step is fed as an input to the current step. The idea is to use the previous output as a form of memory, allowing the network to maintain some context of the input sequence.

However, the training of RNNs can be challenging due to the vanishing gradient problem. This occurs when the gradients become very small as they propagate backwards through time, making it difficult for the network to learn long-term dependencies. Essentially, the gradients become diluted as they propagate backwards, leading to a vanishing gradient problem.

## Long Short-Term Memory (LSTM) Networks
LSTM networks are a type of RNN designed to overcome the vanishing gradient problem by introducing memory cells and gating mechanisms that allow the network to selectively remember or forget information. The memory cells in LSTMs are designed to maintain information over long periods of time, and the gating mechanisms allow the network to selectively update or discard information as needed.

LSTMs have a more complex architecture than standard RNNs, consisting of three main components: the input gate, the forget gate, and the output gate. These gates allow the LSTM network to control the flow of information through the network, allowing it to selectively update the memory cells and forget irrelevant information.

### The Input Gate
The input gate determines which information from the input should be stored in the memory cell. It is a sigmoid layer that takes as input the current input and the previous output, and outputs a value between 0 and 1. A value of 0 means that the information is not important and should be ignored, while a value of 1 means that the information is important and should be stored.

### The Forget Gate
The forget gate determines which information from the previous state of the memory cell should be forgotten. It is also a sigmoid layer that takes as input the previous output and the current input, and outputs a value between 0 and 1. A value of 0 means that the information should be forgotten, while a value of 1 means that the information should be kept.

### The Output Gate
The output gate determines which information from the memory cell should be output to the next step of the network. It is a tanh layer that takes as input the previous output and the current input, and outputs a value between -1 and 1. The output gate then multiplies this value with the result of the input gate to determine the final output.

##  Bidirectional LSTM

A Bidirectional Long Short-Term Memory (BLSTM) is a type of Recurrent Neural Network (RNN) that processes a sequence of inputs in both forward and backward directions simultaneously. Unlike a traditional LSTM, which processes the input sequence from left to right, a BLSTM processes the input sequence from left to right and from right to left simultaneously.

![image](https://user-images.githubusercontent.com/78900552/227276376-bc60a4c6-a2bc-4eb1-9144-492909b21606.png)

# Applications

## Stock Predictor
The repository includes three files for the stock predictor application:

- scraper.py: This file uses the Yahoo Finance API to scrape all the necessary data for the chosen stock. The data includes the opening price, closing price, high price, low price, and volume.

- EDA.ipynb: This file contains the Exploratory Data Analysis (EDA) of the chosen stock. It includes visualizations such as line plots, scatter plots, and box plots to understand the trends and patterns in the data.

- predictor.ipynb: This file contains the LSTM model to generate predictions for the chosen stock. The model takes in the historical data and generates predictions for the future closing price of the stock. The file also includes a plot of the predicted values along with the actual values for visual comparison.


# Conclusion

This study provides a comprehensive understanding of LSTM and its applications. The stock predictor application serves as an example of how LSTM can be used for time series prediction. The study can be used as a starting point for further research and implementation of LSTM in various applications.
