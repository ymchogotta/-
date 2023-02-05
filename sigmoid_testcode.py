import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

for i in range(-10, 10, 1):
    print("sigmoid({}) : {}".format(i, sigmoid(i)))
          