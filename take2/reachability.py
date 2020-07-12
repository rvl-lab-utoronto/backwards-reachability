import numpy as np
from math import sin, cos, tan, pi

num_steps = 10

def get_u_new(x, u_old, timestep):
    possible_controls = []
    possible_controls.append(0.)

    if timestep >= 5:
        possible_controls.append(pi/4)

    final = [np.array([0., 0., possible]) for possible in possible_controls]
    return final

A = np.array([[1., -0.5, 0.],
              [1., 1., 0.],
              [0., 0., 1.]])

B = np.array([[0., 0., 0.],
              [0., 0., 0.],
              [0., 0., 1.]])

x_0 = np.array([1., 2., 3.])
u_0 = np.array([0., 0., 0.])

reach = {}
reach[str(x_0)] = "."
queue =[]
queue.append(x_0)

x_prev = x_0
u_prev = u_0

for i in range(num_steps):
    for pn_state in queue: # for each discovered state
        # get all the possible things we could do
        u_outs = get_u_new(pn_state, u_prev, i)        
        # queue.remove(pn_state)
        for u in u_outs:
            print(u)
            pn_x_new = (A @ x_prev) + (B @ u)
            print(pn_x_new)
            if str(pn_x_new) not in reach:
                reach[str(pn_x_new)] = "."
                queue.append(pn_x_new)


for state in reach:
    print(state)


















