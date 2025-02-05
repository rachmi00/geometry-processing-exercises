import gpytoolbox as gpy, polyscope as ps
ps.init()
V,F = gpy.read_mesh("exercise_03\data\penguin.obj")
ps_penguin = ps.register_surface_mesh("penguin", V, F, enabled=True)
V,F =gpy.read_mesh("exercise_03\data\wingnut.obj")
ps_wignut = ps.register_surface_mesh("wignut", V, F)
#ps_wignut.set_enabled(True) sets enabled to true
ps_wignut.remove() #removes wignut
#ps.remove_all_structures() removes all objects 
ps.show()