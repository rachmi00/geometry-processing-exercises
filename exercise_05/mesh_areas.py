import gpytoolbox as gpy, numpy as np, polyscope as ps
V,F = gpy.read_mesh("exercise_05\data\penguin.obj")
A = 0.5 * gpy.doublearea(V,F)
print(f"Total mesh area: {np.sum(A)}")
ps.init()
ps_penguin = ps.register_surface_mesh("penguin", V, F)
ps_penguin.add_scalar_quantity("triangle areas", A,
    defined_on='faces', enabled=True)
ps.show()