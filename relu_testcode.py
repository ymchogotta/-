def relu(x):
    return max(0, x)

for i in range(-10, 10, 1):
    print("relu({}) : {}".format(i, relu(i)))