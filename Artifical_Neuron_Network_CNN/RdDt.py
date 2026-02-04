import random
import numpy as np
import pandas as pd

# Input values
genders = np.array([])#Female,Male
heights = np.array([])
weights = np.array([])
eye_colors = np.array([])#Black,Kahve,Green
hair_colors = np.array([])#Black,Yellow,Red

random_data = 100
for i in range(random_data):
    genders = np.append(genders,np.random.randint(0,2))
    heights = np.append(heights,random.uniform(0,1))
    weights = np.append(weights,random.uniform(0,1))
    eye_colors = np.append(eye_colors,(np.random.randint(0,3)/3))#Black,Kahve,Green
    hair_colors = np.append(hair_colors,(np.random.randint(0, 3)/3))#Black,Yellow,Red
data = {
    "Genders": genders,
    "Heights": heights,
    "Weights": weights,
    "Eye_Colors": eye_colors,
    "Hair_Colors": hair_colors
}

df = pd.DataFrame(data)
df.to_csv('in.csv')