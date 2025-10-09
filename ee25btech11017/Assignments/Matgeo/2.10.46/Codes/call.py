import numpy as np
import matplotlib.pyplot as plt
import ctypes

# Load shared library
lib = ctypes.CDLL('./vector_cross.so')

# Call function to compute cross product
lib.compute_cross_product()

# Set return type for function returning array pointer
lib.get_cross_product.restype = ctypes.POINTER(ctypes.c_double)

# Get pointer to cross product array
cross_ptr = lib.get_cross_product()

# Extract cross product components into numpy array
cross_product = np.ctypeslib.as_array(cross_ptr, shape=(3,))

# Vectors V and W (defined same as in C)
V = np.array([2, 1, -1])
W = np.array([1, 0, 3])

# Plot vectors and the cross product vector
origin = np.zeros(3)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.quiver(*origin, *V, color='blue', label='V')
ax.quiver(*origin, *W, color='green', label='W')
ax.quiver(*origin, *cross_product, color='red', label='V x W (from C)')

ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('Vectors V, W and Cross Product V x W from C code')

ax.legend()
plt.show()

