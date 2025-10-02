import numpy as np
import matplotlib.pyplot as plt
from ctypes import CDLL, c_double, POINTER

# Load the shared library
lib = CDLL('./projection.so')

# Define argument and return types for the projection function
lib.vector_projection.argtypes = [POINTER(c_double), POINTER(c_double), POINTER(c_double)]

# Create numpy arrays for vectors a and b
a = np.array([2.0, 3.0, 2.0], dtype=np.double)
b = np.array([1.0, 2.0, 1.0], dtype=np.double)

# Prepare array to store the projection vector
proj = np.zeros(3, dtype=np.double)

# Call the C function
lib.vector_projection(a.ctypes.data_as(POINTER(c_double)),
                      b.ctypes.data_as(POINTER(c_double)),
                      proj.ctypes.data_as(POINTER(c_double)))

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vector a
ax.quiver(0, 0, 0, a[0], a[1], a[2], color='r', label='Vector a')

# Plot vector b
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='b', label='Vector b')

# Plot projection of a on b
ax.quiver(0, 0, 0, proj[0], proj[1], proj[2], color='g', label='Projection of a on b')

# Setting the plot limits
max_val = max(np.linalg.norm(a), np.linalg.norm(b)) + 1
ax.set_xlim([0, max_val])
ax.set_ylim([0, max_val])
ax.set_zlim([0, max_val])

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.legend()
plt.title('Vector Projection from C code')
plt.show()

