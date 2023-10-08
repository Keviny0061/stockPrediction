import torch
import numpy as np
from model import CustomLinearRegression
from data_loader import custom_load_data
import training_utils
from sys import argv
#input_data = argv[1]
# #print(input_data)
#print("Input one number")
#num = input()
#print(f"hello {num}")
x_data, y_data = custom_load_data('output.txt')
print("Entered load data")
model = CustomLinearRegression(input_dim=1)
print("built custom model")
print("right before training utils is called")
training_utils.train_model(model, x_data, y_data)
