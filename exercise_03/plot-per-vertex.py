import gpytoolbox as gpy, polyscope as ps
V,F = gpy.icosphere(1)
per_vertex_y_coord = V[:,1]
per_face_y_coord = (V[F[:,0],1]+V[F[:,1],1]+V[F[:,2],1])/3.
ps.init()
ps_sphere1 = ps.register_surface_mesh("sphere1", V, F)
ps_sphere1.add_scalar_quantity("per vertex y coord", per_vertex_y_coord,
    defined_on='vertices', enabled=True)
ps_sphere2 = ps.register_surface_mesh("sphere2", V, F)
ps_sphere2.add_scalar_quantity("per face y coord", per_face_y_coord,
    defined_on='faces', enabled=True)
ps.show()