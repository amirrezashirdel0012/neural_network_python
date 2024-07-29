# make a network which has 3 inputs with 4 neurons
# p = R*1   => R = 3  p1, p2, p3    p = [p1, p2, p3]T
# S = 4, R = 3

# p1 = 0.5, p2 = 1.75, p3 = -1
# w11 = 0, w12 = 0.5, w13 = 1.5, w21 = 1.5, w22 = -0.5, w23 = -0.75, w31 = 0, w32 = 2, w33 = 0, w41 = 0.5, w42 = 0.5, w43 = 0
# b1 = 0, b2 = -0.5, b3 = 0.5, b4 = 1

# W = [
#     w11, w12, w13
#     w21, w22, w23
#     w31, w32, w33
#     w41, w42, w43
#     ] S * R = 4 * 3

# p = [
#     p1
#     p2
#     p3
# ] R * 1 = 3 * 1

# b = [
#     b1
#     b2
#     b3
#     b4
#     ] S * 1 = 4 * 1

# n = W * p + b = (S * R = 4 * 3) * (R * 1 = 3 * 1) + (S * 1 = 4 * 1) => (S * 1 = 4 * 1)

# a = f(n) S * 1 = 4 * 1

# f = hardlim   n < 0 => a = 0, n >= 0 => a = 1

import numpy as np

def hardlim (n):
    x, y = n.shape

    a = np.zeros([x, y])

    for i in range(x):
        for j in range(y):
            if n[i][j] < 0:
                a[i][j] = 0
            else:
                a[i][j] = 1
    return a

w11 = 0 
w12 = 0.5
w13 = 1.5
w21 = 1.5
w22 = -0.5
w23 = -0.75
w31 = 0
w32 = 2
w33 = 0
w41 = 0.5
w42 = 0.5
w43 = 0

p1 = 0.5
p2 = 1.75
p3 = -1

b1 = 0
b2 = -0.5
b3 = 0.5
b4 = 1

W = np.array([
    [w11, w12, w13],
    [w21, w22, w23],
    [w31, w32, w33],
    [w41, w42, w43]
])

p = np.array([
    [p1],
    [p2],
    [p3]
])

b = np.array([
    [b1],
    [b2],
    [b3],
    [b4]
])


n = np.matmul(W, p)+ b

a = hardlim(n)

print("W: ")
print(W)
print("p: ")
print(p)
print("b: ")
print(b)
print("n: ")
print(n)
print("a: ")
print(a)

