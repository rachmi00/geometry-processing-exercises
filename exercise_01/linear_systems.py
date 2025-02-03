import numpy as np
import scipy as sp

#Linear equations
A = np.array([[1., 2.], [3., 4.]])
b = np.array([-2, -3])
print(f"inv(A)@b = {np.linalg.solve(A,b)}")

#Sparce matrices
i = np.array([0,1,1,2])
j = np.array([0,1,2,2])
k = np.array([1., -1., -2., 1.])
Am = sp.sparse.csr_matrix((k, (i,j)), shape=(3,3)) #the shape tuple is the dimension of A
print(f"A = {Am.todense()}")
i = np.array([0,0,1,2])
j = np.array([0,1,2,1])
k = np.array([-2., -1., 2., 1.])
B = sp.sparse.csr_matrix((k, (i,j)), shape=(3,3))
print(f"A+B = {(Am+B).todense()}")
print(f"A*B = {(Am*B).todense()}")
