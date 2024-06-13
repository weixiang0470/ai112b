import torch
import torch.nn as nn
import torch.nn.functional as F
# lenet: 參考 https://medium.com/ching-i/%E5%8D%B7%E7%A9%8D%E7%A5%9E%E7%B6%93%E7%B6%B2%E7%B5%A1-cnn-%E7%B6%93%E5%85%B8%E6%A8%A1%E5%9E%8B-lenet-alexnet-vgg-nin-with-pytorch-code-84462d6cf60c
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=10, kernel_size=5)
        self.conv2 = nn.Conv2d(in_channels=10, out_channels=20, kernel_size=5)
        self.conv_drop = nn.Dropout2d()

        self.fc1 = nn.Linear(in_features=16*5*2*2, out_features=250)
        self.fc2 = nn.Linear(in_features=250, out_features=100)
        self.fc3 = nn.Linear(in_features=100, out_features=10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv_drop(self.conv1(x)),2))
        x = F.relu(F.max_pool2d(self.conv_drop(self.conv2(x)),2))

        x = x.view(-1, 16*5*2*2)
        #x = torch.flatten(x, 1)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = F.relu(self.fc2(x))
        x = F.dropout(x, training=self.training)
        x = self.fc3(x)
        return x