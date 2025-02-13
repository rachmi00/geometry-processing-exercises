import gpytoolbox as gpy, numpy as np, polyscope as ps
V,F = gpy.read_mesh("exercise_10\data\penguin_low_res.obj")
V1,F1 = gpy.subdivide(V, F, method='loop')
V3,F3 = gpy.subdivide(V, F, method='loop', iters=3)
ps.init()
ps_penguin0 = ps.register_surface_mesh("penguin coarse", V, F,
    material='wax', smooth_shade=True, edge_width=1.)
ps_penguin1 = ps.register_surface_mesh("penguin finer", V1, F1,
    material='wax', smooth_shade=True, edge_width=1.)
ps_penguin3 = ps.register_surface_mesh("penguin finest", V3, F3,
    material='wax', smooth_shade=True, edge_width=1.)
ps.show()