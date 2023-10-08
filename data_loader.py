import torch

def custom_load_data(file_path):
    x_data = []
    y_data = []

    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into two values
            values = line.strip().split(',')
            if len(values) == 2:
                x_data.append([float(values[0])])
                # You can modify this if you need further preprocessing for y_data
                y_data.append(float(values[1]))
                print([float(values[0]), float(values[1])])

    x_data = torch.tensor(x_data, dtype=torch.float32)
    y_data = torch.tensor(y_data, dtype=torch.float32)

    return x_data, y_data