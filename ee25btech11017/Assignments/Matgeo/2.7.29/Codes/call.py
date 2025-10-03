import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load shared library
lib = ctypes.CDLL('./triangle_area.so')

# Set restype for compute_area function
lib.compute_area.restype = ctypes.c_double

# Compute area by calling C function
area = lib.compute_area()
print(f"Area of triangle OAB from C code = {area:.4f}")

# Define vertices O, A, B
O = np.array([0, 0, 0])
A = np.array([1, 2, 3])
B = np.array([-3, -2, 1])

# Plot triangle
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(*O, color='black', label='O (0,0,0)')
ax.scatter(*A, color='blue', label='A (1,2,3)')
ax.scatter(*B, color='green', label='B (-3,-2,1)')

# Plot edges
ax.plot([O[0], A[0]], [O[1], A[1]], [O[2], A[2]], 'b')
ax.plot([O[0], B[0]], [O[1], B[1]], [O[2], B[2]], 'g')
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], 'r')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'Triangle OAB with Area = {area:.4f} (from C code)')
ax.legend()
plt.show()

