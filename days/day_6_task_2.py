import numpy as np

data = open('../inputs/day_6').readlines()
data = map(lambda line: list(line[0:8]), data)
data = np.array(data).transpose()
print(data.shape)

def most_common(vector):
    (values, counts) = np.unique(vector, return_inverse=True)
    return values[np.argmin(np.bincount(counts))]

print(''.join(np.apply_along_axis(most_common, axis=1, arr=data)))




