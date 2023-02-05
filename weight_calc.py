import numpy as np

'''
A = np.array([1, 2, 3])
B = np.array([2, 2, 2])
print(np.matmul(A, B.T))

C = np.array([[1, 2, 3],
               [4, 5, 6]])
D = np.array([1, 1, 0])
print(np.matmul(C, D.T))
'''

# p.93

## 1
X = np.array([[-1.7, -10.3, 0, 0, 1, 1], 
              [-7.7, 4.7, 0, 1, 0, 1], 
              [9.3, 5.7, 0, 0, 1, 1]])

## 2
W1 = np.array([1, 3, 3, 10, 0.5, 30])

## 3
print(np.matmul(X, W1.T))

## 4
W2 = np.array([[1, 3, 3, 10, 0.5, 10],
             [-1, 3, 3, 10, 0.5, 20], 
             [1, 3, 3, -10, 0.5, 30]])

print(np.matmul(X, W2.T))
