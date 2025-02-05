import numpy as np, polyscope as ps, gpytoolbox as gpy
V, F = gpy.read_mesh('exercise_02\data\penguin.obj')

ps.init()
ps.register_surface_mesh("mesh", V, F)
ps.show()