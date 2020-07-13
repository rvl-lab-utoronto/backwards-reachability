import numpy as np
from math import sin, cos, tan, pi
from itertools import product

# EXCLUDE_CONTROL cannot be true if BACKWARD is true
EXCLUDE_CONTROL = False
BACKWARD = True

num_steps = 10
control_sp = [-1., 0., 1.]
# control_sp = [0., 1.]


def get_u_new_p(x, u_old, timestep):
    possible_controls = control_sp
    options = product(possible_controls, repeat=2)

    final = [np.array([0., 0.,] + list(option)) for option in options]
    return final

# I'm not sure if we need a 4x4 matrix here
# At least for these simple dynamics, 
# the two bottom rows are redundant as they don't affect anything 
A = np.array([[1., 0., 1., 0.],
              [0., 1., 0., 1.],
              [0., 0., 1., 0.],
              [0., 0., 0., 1.]])

bA = np.linalg.inv(A)

B = np.array([[0., 0., 0., 0.],
              [0., 0., 0., 0.],
              [0., 0., 1., 0.],
              [0., 0., 0., 1.]])

x_0 = np.array([1., 2., 0., 0.])
u_0 = np.array([0., 0., 1., 1.])

print("Initial Conditions:")
print("Dynamics:\n", A)
print("Backward Dynamics:\n", bA)
print("Control Matrix:\n", B)
print("x_0: ", x_0)
print("u_0: ", u_0, "\n\n")


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
            print("curr x:", pn_state)
            print("curr u: ", u)
            Bu = B @ u

            if BACKWARD:
                x__Bu = pn_state - Bu
                pn_x_new = bA @ (x__Bu)
                print("x__Bu: ", x__Bu)
            else:
                Ax = A @ pn_state
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
        if count > 20:
            break
        
for idx, state in enumerate(reach):
    print(idx, state)

















