import torch
import torch.nn as nn

class CustomLinearRegression(nn.Module):
    def __init__(self, input_dim):
        super(CustomLinearRegression, self).__init__()
        self.linear = nn.Linear(input_dim, 1)

    def forward(self, x):
        return self.linear(x)

# Rest of your code remains the same