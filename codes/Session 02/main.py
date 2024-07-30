import NNTF_file as TF
import numpy as np

### Exercise 2.3

# b = -3
# w = 1

# TF = TF.NNTF()
  
# p = 5
# n = w*p+b
# a = TF.hardlims(n)
# print('for p > 3 = ', a)

# p = 2
# n = w*p+b
# a = TF.hardlims(n)
# print('for p < 3 = ', a)


### Perceptron Network example

# Orange
p1 = np.array([
    [1],
    [-1],
    [-1]
])

# apple
p2 = np.array([
    [1],
    [1],
    [-1]
])

W = np.array([
    [0, 1, 0]
])

b = 0

tf = TF.NNTF()

n = np.matmul(W, p1) + b
a = tf.hardlims(n)
print(a)

n = np.matmul(W, p2) + b
a = tf.hardlims(n)
print(a)