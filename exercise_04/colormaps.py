import gpytoolbox as gpy, polyscope as ps
V,F = gpy.read_mesh("exercise_04\data\penguin.obj")
per_vertex_y_coord = V[:,1]
ps.init()
ps_penguin = ps.register_surface_mesh("penguin", V, F)
ps.load_color_map("PuBu", "exercise_04\data\PuBu.png")
ps_penguin.add_scalar_quantity("per vertex y coord", per_vertex_y_coord,
    enabled=True, cmap='PuBu')
ps.show()