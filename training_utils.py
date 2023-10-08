import torch
import torch
import torch.nn as nn
import torch.optim as optim
print("right before entering the def for train_model")
def train_model(model, x_data, y_data, num_epochs=1000):
    print("Right before criterion")
    criterion = nn.MSELoss()
    print("right before optimizer")
    optimizer = optim.SGD(model.parameters(   ), lr=0.01)
    print("Right before for loop")
    for epoch in range(num_epochs):
        outputs = model(x_data)


        loss = criterion(outputs, y_data)


        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 100 == 0:
            print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

    print("Training finished.")