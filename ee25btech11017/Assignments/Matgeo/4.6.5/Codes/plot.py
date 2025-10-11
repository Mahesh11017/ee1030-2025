import numpy as np
import matplotlib.pyplot as plt

# Given line: r = (i + j) + lambda(2i - j + k)
point1 = np.array([1, 1, 0])  # position vector (i + j)
direction1 = np.array([2, -1, 1])  # direction vector

# Required line passing through (2, 1, -1) and parallel to given line
point2 = np.array([2, 1, -1])
direction2 = direction1.copy()

# Function to parameterize points on line
def line_points(point, direction, t_range):
    return np.array([point + t * direction for t in t_range])

# Generate points on both lines
lambda_range = np.linspace(-5, 5, 100)
line1_points = line_points(point1, direction1, lambda_range)
line2_points = line_points(point2, direction2, lambda_range)

# Compute distance between two skew lines using formula:
# distance = |(P2 - P1) . (d1 x d2)| / |d1 x d2|
P2_minus_P1 = point2 - point1
cross_d1_d2 = np.cross(direction1, direction2)
cross_norm = np.linalg.norm(cross_d1_d2)

if cross_norm == 0:
    # Lines are parallel
    distance = np.linalg.norm(np.cross(P2_minus_P1, direction1)) / np.linalg.norm(direction1)
else:
    distance = abs(np.dot(P2_minus_P1, cross_d1_d2)) / cross_norm

print(f"Distance between the two lines = {distance:.4f}")

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(line1_points[:,0], line1_points[:,1], line1_points[:,2], label='Given line')
ax.plot(line2_points[:,0], line2_points[:,1], line2_points[:,2], label='Required line (parallel)')

ax.scatter(*point1, color='blue')
ax.scatter(*point2, color='green')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'Distance between lines = {distance:.4f}')
ax.legend()
plt.show()

