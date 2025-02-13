import gpytoolbox as gpy
import polyscope as ps

# Load the mesh
# Use a raw string (prefix 'r') or double backslashes to avoid escape sequence warnings
V, F = gpy.read_mesh(r"simple_mesh_simplifier\data\penguin.obj")

# Initialize polyscope
ps.init()

# Register the original mesh
ps_mesh = ps.register_surface_mesh("Original Mesh", V, F)

# Show the original mesh
ps.show()

# Get user input for target faces
target_faces = int(input("Enter the target number of faces: "))

# Simplify the mesh
# The decimate function may return more than two values, so we unpack only the first two
result = gpy.decimate(V, F, target_faces)
V_simplified = result[0]  # Simplified vertices
F_simplified = result[1]  # Simplified faces

# Register the simplified mesh
ps_simplified = ps.register_surface_mesh(f"Simplified Mesh ({target_faces} faces)", V_simplified, F_simplified)

# Show both meshes
ps.show()

# Save the simplified mesh
gpy.write_mesh(f"simplified_penguin_{target_faces}.obj", V_simplified, F_simplified)