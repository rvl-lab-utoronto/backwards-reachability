import numpy as np

X = np.random.rand(5, 3)

print(X)

U, S, V = np.linalg.svd(X, full_matrices=True)

print("U: " + str(U))
print("S: " + str(S))
print("V: " + str(V))


Uhat, Shat, Vhat = np.linalg.svd(X, full_matrices=False)

print("Uhat: " + str(Uhat))
print("Shat: " + str(Shat))
print("Vhat: " + str(Vhat))
