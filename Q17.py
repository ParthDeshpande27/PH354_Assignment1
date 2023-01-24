# Exercise 17: Mandelbrot set

import numpy as np
import matplotlib.pyplot as plt

# Recurrence equation = z_n+1 = z^2 + c

# Generating the grid that we will work with (N=1000 took about 8 seconds)
N = 1000
n_iter = 100
xmin = -2
xmax = 2
ymin = -2
ymax = 2
x = np.linspace(xmin, xmax, N)
y = np.linspace(ymin, ymax, N)

def indicator(w, n_iter):
    z = 0
    ind = 1
    for idx in range(n_iter):
        z = z**2 + w
        if abs(z) > 2:
            ind = 0
            break
    return ind

z = np.zeros((N,N))

for idx in range(len(x)):
    for idx2 in range(len(y)):
        z[idx2][idx] = indicator(x[idx]+y[idx2]*1j, n_iter)

h = plt.contourf(x, y, z, cmap='Greys')
plt.axis('square')
plt.title('Mandelbrot set')
plt.tight_layout()
plt.show()
