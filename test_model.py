import pandas as pd
import os
import PIL
import torch.nn as nn
import numpy as np
import torch
import torchvision.models as models

model = torch.load(r'my_project\train-cls\try1\last.pt')
# model = models.resnet152(pretrained=True)
print(model)