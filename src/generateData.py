import json

import numpy as np

normal_set1 = np.random.normal(loc=15, scale=10, size=200)  # Threshold = 85-90
uniform_set1 = np.random.uniform(low=-1, high=1, size=200)
dataset = np.concatenate((normal_set1, uniform_set1))
with open("dataset.txt", "w") as fw:
    json.dump(dataset.tolist(), fw)
