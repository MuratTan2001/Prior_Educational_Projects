#!/usr/bin/env python
# coding: utf-8

# In[510]:


import numpy as np
import random

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
# Training input values
genders = np.array([1,0,1,0])#Female,Male
heights = np.array([180,165,178,163])
weights = np.array([73,60,70,58])
eye_colors = np.array([0,2,1,2])#Black,Kahve,Green
hair_colors = np.array([0,0,1,1])#Black,Yellow,Red
passed = False
result=""
hidden_weights=0
hidden_bias=0
decision_weight=0
decision_bias=0
while passed == False:
    passed = True
    for i in genders:
        n=0
        n=n+1
        # Random weights and bias for the hidden layer
        hidden_weights = np.random.uniform(-1, 1, 4)
        hidden_bias = random.uniform(-1, 1)*4
        
        # Calculate the output of the hidden layer
        hidden_output = np.dot(np.array([heights[n], weights[n], eye_colors[n], hair_colors[n]]), hidden_weights) + hidden_bias
        # Apply sigmoid activation function
        hidden_output_sigmoid = sigmoid(hidden_output)
        
        # Random bias for the final decision
        decision_weight = np.random.uniform(-1,1)
        decision_bias = random.uniform(-1, 1)
        
        # Calculate the output of the desicion layer
        desicion_output = hidden_output_sigmoid * decision_weight + decision_bias

        # Apply sigmoid activation function again
        desicion_output_sigmoid = sigmoid(desicion_output)
        # Make the final decision
        if desicion_output_sigmoid >= 0.5:
            result = "Male"
            result_predict=1
        elif desicion_output_sigmoid < 0.5:
            result = "Female"
            result_predict=0
        else:
            print("Houston, we have a problem.")
            result = "Error"
            break;
        if result_predict != genders[n]:
            passed = False
            break;
    if result == "Error":
        break;
if result == "Error":
    print("Houston, we have a problem.")
    
# Test input values
height = 175
weight = 65
eye_color = 0#Black,Kahve,Green
hair_color = 2#Black,Yellow,Red
# Calculate the output of the hidden layer
hidden_output = np.dot(np.array([height, weight, eye_color, hair_color]), hidden_weights) + hidden_bias

# Apply sigmoid activation function
hidden_output_sigmoid = sigmoid(hidden_output)

# Calculate the output of the desicion layer
desicion_output = hidden_output_sigmoid * decision_weight + decision_bias

# Apply sigmoid activation function again
desicion_output_sigmoid = sigmoid(desicion_output)
# Make the final decision
if desicion_output_sigmoid >= 0.5:
    result = "Male"
    result_predict=1
elif desicion_output_sigmoid < 0.5:
    result = "Female"
    result_predict=0
else:
    print("Houston, we have a problem.")
    result = "Error"
    
print("\n\nTesting values:")
print("Height:", height)
print("Weight:", weight)
print("Eye Color:", eye_color)
print("Hair Color:", hair_color)
print("\nHidden Weights:", hidden_weights)
print("Hidden Bias:", hidden_bias)
print("\nHidden Layer Output (before activation):", hidden_output)
print("Hidden Layer Output (after sigmoid activation):", hidden_output_sigmoid)
print("\nDesicion Weight:", decision_weight)
print("Desicion Bias:", decision_bias)
print("\nDesicion Layer Output (before activation):", desicion_output)
print("Desicion Layer Output (after sigmoid activation):", desicion_output_sigmoid)
print("Final Decision:", result)

# Random input values
gender = np.random.randint(0,2)
height = random.uniform(150, 190)
weight = random.uniform(50, 100)
eye_color = np.random.randint(0, 3)#Black,Kahve,Green
hair_color = np.random.randint(0, 3)#Black,Yellow,Red
# Calculate the output of the hidden layer
hidden_output = np.dot(np.array([height, weight, eye_color, hair_color]), hidden_weights) + hidden_bias

# Apply sigmoid activation function
hidden_output_sigmoid = sigmoid(hidden_output)

# Calculate the output of the desicion layer
desicion_output = hidden_output_sigmoid * decision_weight + decision_bias

# Apply sigmoid activation function again
desicion_output_sigmoid = sigmoid(desicion_output)
# Make the final decision
if desicion_output_sigmoid >= 0.5:
    result = "Male"
    result_predict=1
elif desicion_output_sigmoid < 0.5:
    result = "Female"
    result_predict=0
else:
    print("\nHouston, we have a problem.")
    result = "Error"
    
print("\n\nRandom Input values:")
print("Real Output:", gender)
print("Height:", height)
print("Weight:", weight)
print("Eye Color:", eye_color)
print("Hair Color:", hair_color)
print("\nHidden Weights:", hidden_weights)
print("Hidden Bias:", hidden_bias)
print("\nHidden Layer Output (before activation):", hidden_output)
print("Hidden Layer Output (after sigmoid activation):", hidden_output_sigmoid)
print("\nDesicion Weight:", decision_weight)
print("Desicion Bias:", decision_bias)
print("\nDesicion Layer Output (before activation):", desicion_output)
print("Desicion Layer Output (after sigmoid activation):", desicion_output_sigmoid)
print("Final Decision:", result)
if gender == result_predict:
    print("Success")
else: print("Failure")


# In[ ]:




