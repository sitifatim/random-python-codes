#checking torch versioan
import torch
print(torch.__version__)

#example
import torch
#declare floating-point scalars
x = torch.tensor(2.5)
y = torch.tensor(1.4)
z = torch.add(x,y)
print(z)

#example of using torch with mlp model
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(8,12),
    nn.ReLU(),
    nn.Linear(12,8),
    nn.ReLU(),
    nn.Linear(8,1),
    nn.Sigmoid()
    )

print(model)

import numpy as np
import torch.optim as optim
import pandas as pd

data = pd.read_csv('/content/pima-indians-diabetes.csv')

data

dataset = np.loadtxt('/content/pima-indians-diabetes.csv', delimiter=',')
dataset

X = dataset[:,:8]
Y = dataset[:,-1]
x = torch.tensor(X, dtype=torch.float32)
y = torch.tensor(Y, dtype=torch.float32).reshape(-1,1)

loss_ = nn.BCELoss()
opt = optim.Adam(model.parameters(), lr=0.001)

epoch = 100
batch = 15

for ep in range(epoch):
  for i in range(0, len(x), batch):
    Xbatch = x[i:i+batch]
    y_pred = model(Xbatch)
    Ybatch = y[i:i+batch]
    loss = loss_(y_pred, Ybatch)
    opt.zero_grad()
    loss.backward()
    opt.step()
  print(f'selesai traiining {ep} dengan loss {loss}')

