import numpy as np
from math import sin, cos, tan, pi
import control

num_steps = 10

A = np.array([[1., 0., -0.5],
              [1., 1., -1.],
              [0., 0., 1.]])

B = np.array([[1., 0., -0.5],
              [1., 1., -1.],
              [0., 0., 1.]])

x_0 = np.array([1, 2, 3])

path = []

# METHOD 1

path.append(x_0)
x_prev = x_0

for i in range(num_steps):
    x_new = A @ x_prev
    path.append(x_new)
    x_prev = x_new

for step in path:
    print(step)

# METHOD 2: Compute end directly
