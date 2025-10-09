import numpy as np
import matplotlib.pyplot as plt

# Line equation: x + 2y = 6
# Solve for y: y = (6 - x)/2

x = np.linspace(0, 7, 100)
y = (6 - x)/2

# Normal vector
n = np.array([1, 2])
# Direction vector (perpendicular to normal)
d = np.array([2, -1])

# Plot line
plt.plot(x, y, label='Line: x + 2y = 6')

# Plot normal vector starting from point (3, 1.5) on the line (since 3 + 2*1.5=6)
origin = np.array([3, 1.5])

plt.quiver(*origin, *n, color='red', scale=3, label='Normal vector n = (1, 2)')
plt.quiver(*origin, *d, color='green', scale=3, label='Direction vector d = (2, -1)')

plt.xlim(0, 7)
plt.ylim(0, 5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line with normal and direction vectors')
plt.grid(True)
plt.legend()
plt.show()

