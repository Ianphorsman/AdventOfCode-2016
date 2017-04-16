import numpy as np

data = np.loadtxt('../inputs/day_3').T.reshape(-1, 3).T
data.sort(axis=0)
print(np.sum(sum(data[:2]) > data[2]))