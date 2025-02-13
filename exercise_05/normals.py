import gpytoolbox as gpy, numpy as np, polyscope as ps
V,F = gpy.icosphere(2)
Nv = gpy.per_vertex_normals(V,F)
ps.init()
ps_sphere = ps.register_surface_mesh("sphere", V, F)
ps_sphere.add_vector_quantity("per vertex normals", Nv,
    defined_on='vertices', enabled=True)
ps.show()