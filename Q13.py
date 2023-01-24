# Exercise 13: Plotting experimental data

import numpy as np
import matplotlib.pyplot as plt

# Part A
sunspots_data = np.loadtxt(r"sunspots.txt")
x1 = sunspots_data[:, 0]
y1 = sunspots_data[:, 1]

# Part B
x2 = sunspots_data[0:1001, 0]
y2 = sunspots_data[0:1001, 1]

# Part C
def Y_k(y, r):
    Y = 0
    for m in range(-r, r+1):
        Y = y + m
    return (1/2*r)*Y

Y_k = Y_k(y2, 5)

# Creating 2 subplots
figure, axis = plt.subplots(2)

# Accessing each axes object to plot the data through returned array
axis[0].plot(x1, y1)
axis[1].plot(x2, y2)
axis[1].plot(x2, Y_k)

# Combine all the operations and display
plt.xlabel("Month")
plt.ylabel("The number of sunspots")
plt.show()

    

