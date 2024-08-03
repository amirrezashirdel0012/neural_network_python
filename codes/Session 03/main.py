import numpy as np  # import numpy module
import NNTF_file as TF  # import transfer functions module

tf = TF.NNTF()  # invoke TF module

# define p1
p1 = np.array([
    [1],
    [2]
])  
# define p2
p2 = np.array([
    [-1],
    [2]
])  
# define p3
p3 = np.array([
    [0],
    [-1]
])  

# define targets
t1 = 1
t2 = 0
t3 = 0

# initialize weights and bias
W = np.array([[0, 0]])
b = 0


# perceptron rule
for i in range(5):
    # p1
    a1 = tf.hardlim(np.matmul(W, p1) + b)

    e = t1 - a1
    W = W + e*np.transpose(p1)
    b = b + e

    # p2
    a2 = tf.hardlim(np.matmul(W, p2) + b)

    e = t2 - a2
    W = W + e*np.transpose(p2)
    b = b + e

    # p3
    a3 = tf.hardlim(np.matmul(W, p3) + b)

    e = t3 - a3
    W = W + e*np.transpose(p3)
    b = b + e

print(W)
print(b)

print('test')

a1 = tf.hardlim(np.matmul(W, p1) + b)
a2 = tf.hardlim(np.matmul(W, p2) + b)
a3 = tf.hardlim(np.matmul(W, p3) + b)

print(a1, a2, a3)
print(t1, t2, t3)


