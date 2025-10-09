import numpy as np
import matplotlib.pyplot as plt

# Define vectors V and W
V = np.array([2, 1, -1])
W = np.array([1, 0, 3])

# Compute cross product
cross_V_W = np.cross(V, W)

# Plotting the vectors and their cross product
origin = np.zeros(3)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot V
ax.quiver(*origin, *V, color='blue', label='V')

# Plot W
ax.quiver(*origin, *W, color='green', label='W')

# Plot cross product of V and W
ax.quiver(*origin, *cross_V_W, color='red', label='V x W')

# Setting plot limits and labels
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Vectors V, W and Cross Product V x W')

ax.legend()
plt.show()

