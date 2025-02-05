import numpy as np, polyscope as ps
V = np.array([[0.,0.], [1.,0.], [0.,1.],[1.,1.]])
F = np.array([[0, 1, 2], [2,1,3]])
print(f"F = {F}")
ps.init()
ps.register_surface_mesh("mesh", V, F)
ps.show()