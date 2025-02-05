import gpytoolbox as gpy, polyscope as ps
V,F = gpy.read_mesh("exercise_04\data\penguin.obj")
per_vertex_y_coord = V[:,1]
ps.init()
ps_penguin = ps.register_surface_mesh("penguin", V, F)
ps_penguin.add_scalar_quantity("per vertex y coord", per_vertex_y_coord,
    isolines_enabled=True, isoline_width=0.05, isoline_darkness=0.1,
    enabled=True)
ps.show()