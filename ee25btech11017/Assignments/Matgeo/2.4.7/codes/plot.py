import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define vectors
a = np.array([2, 3, 2])
b = np.array([1, 2, 1])

# Calculate projection of a on b
b_norm = b / np.linalg.norm(b)
proj_a_on_b = np.dot(a, b_norm) * b_norm

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vector a
ax.quiver(0, 0, 0, a[0], a[1], a[2], color='r', label='Vector a')

# Plot vector b
ax.quiver(0, 0, 0, b[0], b[1], b[2], color='b', label='Vector b')

# Plot projection of a on b
ax.quiver(0, 0, 0, proj_a_on_b[0], proj_a_on_b[1], proj_a_on_b[2], color='g', label='Projection of a on b')

# Setting the plot limits
max_val = max(np.linalg.norm(a), np.linalg.norm(b)) + 1
ax.set_xlim([0, max_val])
ax.set_ylim([0, max_val])
ax.set_zlim([0, max_val])

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.legend()
plt.title('Vector Projection: a on b')
plt.show()

