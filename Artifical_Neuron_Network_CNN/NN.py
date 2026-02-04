# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:27:56 2024

@author: Ranger
"""

import numpy as np
import pandas as pd
import random

def calculate_accuracy(y_true, y_pred):
    correct_predictions = sum(1 for true, pred in zip(y_true, y_pred) if true == pred)
    accuracy = correct_predictions / len(y_true)
    return accuracy
def binary_cross_entropy(y_true, y_pred):
    epsilon = 1e-15  # To avoid division by zero
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)  # Clip values to avoid numerical instability
    loss = -(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    return np.mean(loss)
class ANN:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights
        self.weights_input_hidden = np.random.uniform(-0.1, 0.1, (input_size, hidden_size))
        self.weights_hidden_output = np.random.uniform(-0.1, 0.1, (hidden_size, output_size))

    def mse(self, y, y_hat):
        # np.mean is better than 1/2 division + array compatibility
        return np.mean((y - y_hat) ** 2)

    def feedforward(self, X):
        # Forward pass
        self.hidden_input = np.dot(X, self.weights_input_hidden)
        self.hidden_output = self.sigmoid(self.hidden_input)
        self.output = np.dot(self.hidden_output, self.weights_hidden_output)
        return self.output

    def backpropagation(self, X, y, learning_rate=0.02):
        # Backpropagation
        output_error = y - self.output
        hidden_error = np.dot(output_error, self.weights_hidden_output.T)
        output_delta = output_error * (self.output * (1 - self.output))
        hidden_delta = hidden_error * (self.hidden_output * (1 - self.hidden_output))

        # Update weights
        self.weights_hidden_output += learning_rate * np.dot(self.hidden_output.T, output_delta)
        self.weights_input_hidden += learning_rate * np.dot(X.T, hidden_delta)

        return output_error

    def train(self, X, y, min_error=0.05, learning_rate=0.05):
        print("Please wait. This might take a while.")
        while True:
            # Forward pass
            y_hat = self.feedforward(X)
            # Calculate error
            error = self.mse(y, y_hat)
            if error < min_error:
                print(f"Training finished with MSE:{error},\nAnd with guesses of :\n{y_hat}")
                break
            # Backpropagation
            self.backpropagation(X, y, learning_rate)
    def test(self,X, y):
        y_hat = self.feedforward(X)
        return y_hat

    def extract(self):
        result= np.array([
            [self.weights_input_hidden],
            [self.weights_hidden_output]
        ])
        return result
    def sigmoid(self, x):
        # Prevent overflow by capping large positive and negative values
        x = np.clip(x, -500, 500)
        return 1 / (1 + np.exp(-x))


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


df = pd.read_csv('in.csv', index_col=0)

y_column = df.iloc[:, 0]
x_columns = df.drop(df.columns[0], axis=1)
split_index = int(0.7 * len(df))

train_x = x_columns.iloc[:split_index]
train_y_array = y_column.iloc[:split_index]
test_x = x_columns.iloc[split_index:]
test_y_array = y_column.iloc[split_index:]


train_y_array = train_y_array.values
train_y =np.array([])
train_y = np.append(train_y,train_y_array[0])
for n in range(1,len(train_y_array)):
    train_y = np.vstack((train_y,train_y_array[n]))


test_y_array = test_y_array.values
test_y = np.array([])
test_y = np.append(test_y,test_y_array[0])
for n in range(1,len(test_y_array)):
    test_y = np.vstack((test_y,test_y_array[n]))

model = ANN(input_size=4, hidden_size=4, output_size=1)
model.train(train_x, train_y)
y_pred = model.test(test_x ,test_y)
print("Real output deducted from predicted output")
print(y_pred)
accuracy = calculate_accuracy(test_y, y_pred)
print("Accuracy:", accuracy)
correlation = np.corrcoef(test_y, y_pred)[0, 1]
print("Correlation:", correlation)
loss = binary_cross_entropy(test_y, y_pred)
print("Loss:", loss)
