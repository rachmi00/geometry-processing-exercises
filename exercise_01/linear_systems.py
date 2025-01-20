import numpy as np
A = np.array([[1., 2.], [3., 4.]])
b = np.array([-2, -3])
print(f"inv(A)@b = {np.linalg.solve(A,b)}")