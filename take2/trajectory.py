import numpy as np
from math import sin, cos, tan
import control


A = np.array([
    # A = [
    [1., 0, cos(1)],
    [0, 1., sin(1)],
    [0, 0, 0]
    # ]
])


# B = np.array(
B = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 1.]
]
# )

C = [[1., 0, 0],
     [0, 1., 0],
     [0, 0, 1.]]

D = [[1., 0, 0],
     [0, 1., 0],
     [0, 0, 1.]]


print(A)

sys = control.ss(A, B, C, D, 1)

T = [i for i in range(10)]
U = [[0, 0, 1] for i in range(10)]

# x_0 = [1., 2., 0]
x_0 = np.array(
    [[1.],
     [2.],
     [1]]
)


x_1 = A @ x_0

print(x_1)
# print(U)

# T, y_out, x_out = control.forced_response(sys, T, U, x_0)
# # y_out, T = control.step_response(sys)
# print("x_out: " + str(x_out))
# print("y_out: " + str(y_out))
# print("T: " + str(T))
