import torch
import numpy as np
from model import CustomLinearRegression
from data_loader import custom_load_data
import training_utils
from sys import argv

# Load your data
x_data, y_data = custom_load_data('output.txt')

# Determine the input dimension based on the number of features in x_data
input_dim = x_data.shape[1]

# Reshape the target tensor to match the shape of predicted values
y_data = y_data.view(-1, 1)

# Create and train the model
model = CustomLinearRegression(input_dim=input_dim)
training_utils.train_model(model, x_data, y_data)

# Function to predict y for a given x
def predict_y(input_x):
    # Create an input tensor with the correct shape
    print("before tensor is created")
    input_x_tensor = torch.tensor([[input_x]], dtype=torch.float32)

    # Use the trained model to predict y
    print(model(input_x_tensor))
    print("after tensor is created")
    predicted_y = model(input_x_tensor)
    print("after tensor is calculated")
    return predicted_y.item()

# Prompt the user for input and calculate y
try:
    input_x = float(input("Enter a value for x: "))
    predicted_y = predict_y(input_x)
    print(f"For x = {input_x}, the predicted y is {predicted_y}")
except ValueError:
    print("Invalid input. Please enter a numeric value for x.")