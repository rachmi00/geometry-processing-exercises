import numpy as np

A = np.array([[1.,2.],[2.,3.],[4.,5.]])
B = np.array([[13.,14.], [15., 16.], [17., 18.]])
u = np.array([7.,8.])

#element wise operations
print(f"A+B: {A+B}")
print(f"B*A: {B*A}")
print(f"A-3: {A-3}")
print(f"1./A: {1./A}")
# matrix multiplication
print(f"A@u matrix multiplication:{A@u}")

#transpose of a matrix
print(f"Transpose A.T:{A.T}")

#Frobenius norm of a matrix
print(f"||A||_F = {np.linalg.norm(A)}")
#Euclidean norm of a vetor u,
print(f"||u|| = {np.linalg.norm(u)}")

