import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load the C shared library
lib = ctypes.CDLL('./line_vectors.so')

# Set return types for functions
lib.get_normal.restype = ctypes.POINTER(ctypes.c_double)
lib.get_direction.restype = ctypes.POINTER(ctypes.c_double)

# Get pointers to vectors
normal_ptr = lib.get_normal()
direction_ptr = lib.get_direction()

# Create numpy arrays from pointers
normal = np.ctypeslib.as_array(normal_ptr, shape=(2,))
direction = np.ctypeslib.as_array(direction_ptr, shape=(2,))

# Define the line points
x = np.linspace(0, 7, 100)
y = (6 - x) / 2

# Point on the line (3, 1.5)
origin = np.array([3, 1.5])

# Plot line and vectors
plt.plot(x, y, label='Line: x + 2y = 6')
plt.quiver(*origin, *normal, color='red', scale=3, label='Normal vector n = (1, 2)')
plt.quiver(*origin, *direction, color='green', scale=3, label='Direction vector d = (2, -1)')

plt.xlim(0, 7)
plt.ylim(0, 5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line with normal and direction vectors from C code')
plt.grid(True)
plt.legend()
plt.show()

