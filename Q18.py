# Exercise 18: Photoelectric effect

import numpy as np
import matplotlib.pyplot as plt

# Part A and B

millikan_data = np.loadtxt(r"millikan.txt")
xval = millikan_data[:, 0]
yval = millikan_data[:, 1]
Ex = np.mean(xval)
Ey = np.mean(yval)
Exx = np.mean(xval**2)
Exy = np.mean(xval*yval)
slope = (Exy - Ex*Ey)/(Exx - Ex**2)
intercept = (Exx*Ey - Ex*Exy)/(Exx - Ex**2)

plt.scatter(xval, yval)

print("Here follow the values of the slope m and intercept c for the best fit line:")
print("m =", end=" ")
print(slope)
print("c =", end=" ")
print(intercept)

# Part C

x = np.linspace(np.min(millikan_data[:, 0]),np.max(millikan_data[:, 0]),1000)
best_y = slope*x + intercept
plt.plot(x, best_y, '-r', label='y=mx+c')
plt.title('Least squares fit to Millikan\'s data')
plt.xlabel('Frequencies in Hertz')
plt.ylabel('Voltages in Volt')
plt.legend(loc='upper left')
plt.grid()

# Part D

# slope = h/e ---> h = slope * e

h_experimental = slope*1.602e-19
h_accepted = 6.62607015e-34
deviation = 100*(h_experimental - h_accepted)/h_accepted
print("h_experimental")
print(h_experimental)
print("h_accepted")
print(h_accepted)
print("%Deviation")
print(deviation)

plt.show()
