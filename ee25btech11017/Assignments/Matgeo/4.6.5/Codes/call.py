import ctypes
import numpy as np
import matplotlib.pyplot as plt

lib = ctypes.CDLL('./line_distance.so')

# Initialize C arrays for points and direction
ArrayType3 = ctypes.c_double * 3
P1 = ArrayType3()
P2 = ArrayType3()
direction = ArrayType3()

# Get points and direction from C
lib.get_P1(P1)
lib.get_P2(P2)
lib.get_direction(direction)

lib.compute_distance()
distance = lib.get_distance()

print(f"Distance between lines from C code = {distance:.4f}")

point1 = np.array(list(P1))
point2 = np.array(list(P2))
dir_vec = np.array(list(direction))

# Parameterize lines
lambda_range = np.linspace(-5, 5, 100)
line1_points = np.array([point1 + t * dir_vec for t in lambda_range])
line2_points = np.array([point2 + t * dir_vec for t in lambda_range])

# Plot lines
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(line1_points[:,0], line1_points[:,1], line1_points[:,2], label='Given line')
ax.plot(line2_points[:,0], line2_points[:,1], line2_points[:,2], label='Required line (parallel)')
ax.scatter(*point1, color='blue', label='Point on given line')
ax.scatter(*point2, color='green', label='Point on required line')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'Distance between lines = {distance:.4f}')
ax.legend()
plt.show()

