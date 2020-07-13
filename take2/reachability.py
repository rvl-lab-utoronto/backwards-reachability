import numpy as np
from math import sin, cos, tan, pi
from itertools import product

EXCLUDE_CONTROL = True

num_steps = 10
# control_sp = [-1., 0., 1.]
control_sp = [0., 1.]


def get_u_new_p(x, u_old, timestep):
    possible_controls = control_sp
    options = product(possible_controls, repeat=2)

    final = [np.array([0., 0.,] + list(option)) for option in options]
    return final

A = np.array([[1., 0., 1., 0.],
              [0., 1., 0., 1.],
              [0., 0., 0., 0.],
              [0., 0., 0., 0.]])

B = np.array([[0., 0., 1., 0.],
              [0., 0., 0., 1.],
              [0., 0., 0., 0.],
              [0., 0., 0., 0.]])

x_0 = np.array([1., 2., 0., 0.])
u_0 = np.array([0., 0., 1., 1.])

reach = {}
if EXCLUDE_CONTROL:
    reach[str(x_0[:2])] = "."
else:
    reach[str(x_0)] = "."

queue =[]
queue.append(x_0)

x_prev = x_0
u_prev = u_0

count = 0
for i in range(num_steps):
    print("i: ", i)
    while queue:
        pn_state = queue.pop(0)
        # get all the possible things we could do
        print("=============")
        print("curr op st: ", pn_state)
        u_outs = get_u_new_p(pn_state, u_prev, i)        
        # queue.remove(pn_state)
        for u in u_outs:
            print("====")
            print("curr u: ", u)
            Ax = A @ pn_state
            Bu = B @ u
            pn_x_new = Ax + Bu
            print("Ax: ", Ax )
            print("Bu: ", Bu)
            print("pn_x_new: ", pn_x_new)

            if EXCLUDE_CONTROL:
                check = str(pn_x_new[:2])
            else:
                check = str(pn_x_new)

            if check not in reach:
                print("new state!")
                reach[check] = "."
                queue.append(pn_x_new)

        count += 1
        if count > 1000:
            break
        
for idx, state in enumerate(reach):
    print(idx, state)

















