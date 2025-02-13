import gpytoolbox as gpy, numpy as np, polyscope as ps
V,F = gpy.read_mesh("exercise_05\data\penguin.obj")
k = gpy.angle_defect(V,F)
ps.init()
ps_penguin = ps.register_surface_mesh("penguin", V, F,
    material='wax', smooth_shade=True)
ps_penguin.add_scalar_quantity("angle defect", k,
    vminmax=(-0.15,0.15), cmap='coolwarm', enabled=True)
ps.show()