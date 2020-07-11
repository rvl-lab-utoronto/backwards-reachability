import numpy as np
from math import sin, cos, tan, pi
# import control

num_steps = 10

def get_u_new(x, u_old, timestep):
    control = 0.
    if timestep >= 5:
        control = pi/4
    return np.array([0., 0., control])

A = np.array([[1., -0.5, 0.],
              [1., 1., 0.],
              [0., 0., 1.]])

B = np.array([[0., 0., 0.],
              [0., 0., 0.],
              [0., 0., 1.]])

x_0 = np.array([1., 2., 3.])
u_0 = np.array([0., 0., 0.])

path = []

# METHOD 1

path.append(x_0)
x_prev = x_0
u_prev = u_0

for i in range(num_steps):
    print(A @ x_prev)
    print(B @ u_prev)
    x_new = (A @ x_prev) + (B @ u_prev)
    path.append(x_new)
    x_prev = x_new
    u_prev = get_u_new(x_new, u_prev, i)


for step in path:
    print(step)

# METHOD 2: Compute end directly
