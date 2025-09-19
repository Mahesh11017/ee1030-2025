import matplotlib.pyplot as plt
from ctypes import cdll, POINTER, c_float

# Load shared library
lib = cdll.LoadLibrary('./distance.so')

# Specify return type of get_roots as pointer to array of 2 floats
lib.get_roots.restype = POINTER(c_float * 2)

# Call the C function to get roots
roots_ptr = lib.get_roots()
x1, x2 = roots_ptr.contents[0], roots_ptr.contents[1]

Q = (0, 1)
P = (5, -3)
s = 6  # y-coordinate of R

R1 = (x1, s)
R2 = (x2, s)

# Plotting
plt.scatter(*Q, color='red', label='Q (0,1)')
plt.scatter(*P, color='blue', label='P (5,-3)')
plt.scatter(*R1, color='green', label=f'R1 ({x1:.2f}, 6)')
plt.scatter(*R2, color='green', label=f'R2 ({x2:.2f}, 6)')

plt.plot([Q[0], P[0]], [Q[1], P[1]], 'r--')
plt.plot([Q[0], R1[0]], [Q[1], R1[1]], 'g--')
plt.plot([Q[0], R2[0]], [Q[1], R2[1]], 'g--')

plt.axhline(y=s, color='gray', linestyle=':')
plt.legend()
plt.title('Points Equidistant from Q at y=6 (using C code results)')
plt.grid(True)
plt.axis('equal')
plt.show()

