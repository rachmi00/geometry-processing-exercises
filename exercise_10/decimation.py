import gpytoolbox as gpy, numpy as np, polyscope as ps
V,F = gpy.read_mesh("exercise_10\data\penguin_high_res.obj")
V1,F1,_,_ = gpy.decimate(V, F, face_ratio=0.2)
V2,F2,_,_ = gpy.decimate(V, F, face_ratio=0.05)
ps.init()
ps_penguin0 = ps.register_surface_mesh("penguin fine", V, F,
    material='wax', smooth_shade=True, edge_width=1.)
ps_penguin1 = ps.register_surface_mesh("penguin decimated", V1, F1,
    material='wax', smooth_shade=True, edge_width=1.)
ps_penguin2 = ps.register_surface_mesh("penguin decimated more", V2, F2,
    material='wax', smooth_shade=True, edge_width=1.)
ps.show()