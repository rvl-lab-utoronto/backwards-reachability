import numpy as np
import pandas as pd

from scipy.io import loadmat

X = loadmat('/home/kuwajerw/repos/workstuff/DATA/DATA/FLUIDS/CYLINDER_ALL.mat')

print(type(X))

# print(X.keys('VORTALL'))


print(type(X['VORTALL']))
