import numpy as np
import random


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

    def backpropagation(self, X, y, learning_rate=0.01):
        # Backpropagation
        output_error = y - self.output
        hidden_error = np.dot(output_error, self.weights_hidden_output.T)
        output_delta = output_error * (self.output * (1 - self.output))
        hidden_delta = hidden_error * (self.hidden_output * (1 - self.hidden_output))

        # Update weights
        self.weights_hidden_output += learning_rate * np.dot(self.hidden_output.T, output_delta)
        self.weights_input_hidden += learning_rate * np.dot(X.T, hidden_delta)

        return output_error

    def train(self, X, y, min_error=0.05, learning_rate=0.01):
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

    def sigmoid(self, x):
        # Prevent overflow by capping large positive and negative values
        x = np.clip(x, -500, 500)
        return 1 / (1 + np.exp(-x))


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Input values
genders = np.array([])#Female,Male
heights = np.array([])
weights = np.array([])
eye_colors = np.array([])#Black,Kahve,Green
hair_colors = np.array([])#Black,Yellow,Red

random_data = 5
for i in range(random_data):
    genders = np.append(genders,np.random.randint(0,2))
    heights = np.append(heights,random.uniform(0,1))
    weights = np.append(weights,random.uniform(0,1))
    eye_colors = np.append(eye_colors,(np.random.randint(0,3)/3))#Black,Kahve,Green
    hair_colors = np.append(hair_colors,(np.random.randint(0, 3)/3))#Black,Yellow,Red
input_arrays = np.array([])
y_hat_array = np.array([])
model = ANN(input_size=4, hidden_size=3, output_size=1)
for y_hat in genders:
    n = 0
    n = n + 1
    # Random weights and bias for the hidden layer
    hidden_weights = np.random.uniform(-1, 1, 4)
    hidden_bias = random.uniform(-0.3, 0.3)

    # Calculate the output of the hidden layer
    hidden_output = np.dot(np.array([heights[n], weights[n], eye_colors[n], hair_colors[n]]),
                           hidden_weights) + hidden_bias
    # Apply sigmoid activation function
    hidden_output_sigmoid = sigmoid(hidden_output)

    # Random bias for the final decision
    decision_weight = np.random.uniform(-1, 1)
    decision_bias = random.uniform(-1, 1)

    # Calculate the output of the desicion layer
    desicion_output = hidden_output_sigmoid * decision_weight + decision_bias

    # Apply sigmoid activation function again
    desicion_output_sigmoid = sigmoid(desicion_output)
    print("Real value",y_hat)
    print("Expected Value",desicion_output_sigmoid)
y_hat_array = np.append(y_hat_array,genders[0])
for n in range(1,len(genders)):
    y_hat_array = np.vstack((y_hat_array,genders[n]))
input_arrays = np.stack((heights,weights,eye_colors,hair_colors))
input_arrays = np.column_stack(input_arrays)
input_arrays = np.array(input_arrays)

model.train(input_arrays,y_hat_array)