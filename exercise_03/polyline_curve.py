import gpytoolbox as gpy, polyscope as ps
ps.init()
V,E = gpy.regular_circle_polyline(20)
ps_ring = ps.register_curve_network("ring", V, E)
ps.show()