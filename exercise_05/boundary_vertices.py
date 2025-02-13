import gpytoolbox as gpy, polyscope as ps
V,F = gpy.read_mesh("exercise_05\data\penguin_with_bdry.obj")
bv = gpy.boundary_vertices(F)
print(bv)
ps.init()
ps_penguin = ps.register_surface_mesh("penguin", V, F)
ps_penguin_bdry = ps.register_point_cloud("penguin bdry", V[bv,:])
ps.show()