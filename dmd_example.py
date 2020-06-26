import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from scipy.io import loadmat

# data file is the vorticity fields of the cylinder
# loads the mat file into a dict
DATA = loadmat('./ThirdPartyResources/CYLINDER_ALL.mat')

print(type(DATA))


print(type(DATA['VORTALL']))

# X2 is basically the same as X, except one timestep forward
X = DATA['VORTALL'][:, 1:-1]
X2 = DATA['VORTALL'][:, 2:]

print(type(X))
print(X)

print(type(X2))
print(X2)

# full_matrices=False means it will do an economy SVD
# with a matrix of this size we cant do a full SVD
U, S, V = np.linalg.svd(X, full_matrices=False)

print("U: " + str(U))
print("S: " + str(S))
print("V: " + str(V))


r = 21  # dominant meanflow + 10 harmonic
U = U[:, 1:r]

# the shape of S doesnt match the video, maybe we're getting a diagonal right
# away??
# not sure

# S = S[1:r]  # [1:r, 1:r] ???? honestly just ignore this line
S = np.diag(S)
S = S[1:r, 1:r]
V = V[:, 1:r]

print("\n\n\n now we're resizing \n\n\n")

print("U: " + str(U))
print("S: " + str(S))
print("V: " + str(V))

plt.plot(S)
plt.ylabel('some numbers')
plt.yscale('log')
# plt.show()  # seems to match the video so far


# im sure theres a cleaner way to do this lol
Atilde = U.T @ X2 @ V @ np.linalg.inv(S)

W, eigs = np.linalg.eig(Atilde)


print("\n\n\n eigen stuff \n\n\n")
print("W: " + str(W))
print("eigs: " + str(eigs.shape))

Phi = X2 @ V @ np.linalg.inv(S) @ W
