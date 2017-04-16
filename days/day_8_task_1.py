import numpy as np
import re
import matplotlib.pyplot as p
import seaborn as sns
data = open('../inputs/day_8').readlines()
data = map(lambda line: line.split(), data)

keypad = np.zeros((6, 50))



for line in data:
    command = line[0]
    if command == 'rect':
        dim = re.search('(\d+)x(\d+)', line[1]).groups()
        x = int(dim[0])
        y = int(dim[1])
        keypad[0:y,0:x] = 1
    elif command == 'rotate':
        direction = line[1]
        position = int(re.search('(\d+)', line[2]).group())
        span = int(line[4])
        if direction == 'row':
            keypad[position,0:50] = np.roll(keypad[position,0:50], span)
        elif direction == 'column':
            keypad[0:6,position] = np.roll(keypad[0:6,position], span)


def plot(array, filename):
    p.clf()
    sns.set()
    sns_plot = sns.heatmap(array)
    sns_plot.get_figure().savefig(filename)

plot(keypad[0:6,0:5], 'a')
plot(keypad[0:6,5:10], 'b')
plot(keypad[0:6,10:15], 'c')
plot(keypad[0:6,15:20], 'd')
plot(keypad[0:6,20:25], 'e')
plot(keypad[0:6,25:30], 'f')
plot(keypad[0:6,30:35], 'g')
plot(keypad[0:6,35:40], 'h')
plot(keypad[0:6,40:45], 'i')
plot(keypad[0:6,45:50], 'j')
# ZJHRKCPLYJ
