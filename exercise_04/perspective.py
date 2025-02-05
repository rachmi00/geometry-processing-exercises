import gpytoolbox as gpy, polyscope as ps
V,F = gpy.regular_square_mesh(2)
ps.init()
ps_square = ps.register_surface_mesh("square", V, F)
ps.set_view_projection_mode("orthographic") # switching to orthographic gives us the palin 2d view
ps.show()