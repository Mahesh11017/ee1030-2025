import numpy as np
import matplotlib.pyplot as plt

# Define vectors OA and OB
OA = np.array([1, 2, 3])
OB = np.array([-3, -2, 1])

# Compute cross product
cross = np.cross(OA, OB)
area = 0.5 * np.linalg.norm(cross)

print(f"Area of triangle OAB = {area:.4f}")

# Plot the triangle vertices and edges
origin = np.array([0, 0, 0])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points O, A, B
ax.scatter(*origin, color='black', label='O (0,0,0)')
ax.scatter(*OA, color='blue', label='A (1,2,3)')
ax.scatter(*OB, color='green', label='B (-3,-2,1)')

# Plot edges
ax.plot([origin[0], OA[0]], [origin[1], OA[1]], [origin[2], OA[2]], 'b')
ax.plot([origin[0], OB[0]], [origin[1], OB[1]], [origin[2], OB[2]], 'g')
ax.plot([OA[0], OB[0]], [OA[1], OB[1]], [OA[2], OB[2]], 'r')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title(f'Triangle OAB with Area = {area:.4f}')
ax.legend()
plt.show()

