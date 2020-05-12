import numpy as np
A = np.arange(1,16)
print(A)
B = np.concatenate((A[1:3],A[4:6]))
print(B)