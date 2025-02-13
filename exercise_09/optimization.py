import gpytoolbox as gpy, numpy as np, scipy as sp, polyscope as ps
V,F = gpy.read_mesh("exercise_09\data\penguin.obj")
L = gpy.cotangent_laplacian(V, F)
head_index = 7302
foot_index = 9916
k = np.array([head_index, foot_index])
y = np.array([1., 0.])
Q = gpy.biharmonic_energy(V, F)
u = gpy.min_quad_with_fixed(Q=Q, k=k, y=y)
ps.init()
ps_penguin = ps.register_surface_mesh("penguin", V, F,
    material='wax', smooth_shade=True)
ps_penguin.add_scalar_quantity("u", u, enabled=True)
fixed_cloud = ps.register_point_cloud("fixed", V[k,:])
ps.show()