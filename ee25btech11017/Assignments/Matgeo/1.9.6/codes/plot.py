import matplotlib.pyplot as plt
import numpy as np

# Fixed points Q and P
Q = np.array([0, 1])
P = np.array([5, -3])

# Calculate distance between Q and P
d = np.linalg.norm(P - Q)

# y-coordinate of R
y_R = 6

# Find x-coordinates of points R on line y=6 such that distance(Q, R) = distance(Q, P)
x_R1 = np.sqrt(d**2 - 25)
x_R2 = -x_R1

R1 = np.array([x_R1, y_R])
R2 = np.array([x_R2, y_R])

# Plot points
plt.scatter(*Q, color='red', label='Q (0,1)')
plt.scatter(*P, color='blue', label='P (5,-3)')
plt.scatter(*R1, color='green', label=f'R1 ({x_R1:.2f}, 6)')
plt.scatter(*R2, color='green', label=f'R2 ({x_R2:.2f}, 6)')

# Plot lines from Q to P and Q to R points
plt.plot([Q[0], P[0]], [Q[1], P[1]], 'r--')
plt.plot([Q[0], R1[0]], [Q[1], R1[1]], 'g--')
plt.plot([Q[0], R2[0]], [Q[1], R2[1]], 'g--')

plt.axhline(y=y_R, color='gray', linestyle=':')

plt.legend()
plt.title('Points Equidistant from Q at y=6')
plt.grid(True)
plt.axis('equal')
plt.show()

