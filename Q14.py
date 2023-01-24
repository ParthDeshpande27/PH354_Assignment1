# Exercise 14: Curve plotting

import numpy as np
import matplotlib.pyplot as plt

# Part A
def deltoid(N):
    theta = np.linspace(0, 2 * np.pi, N)
    x = 2 * np.cos(theta) + np.cos(2 * theta)
    y = 2 * np.sin(theta) - np.sin(2 * theta)
    return x, y

x, y = deltoid(1000)
f1 = plt.figure(1)
plt.title("Deltoid")
plt.plot(x, y)

# Part B
def Galilean_spiral(N):
    theta = np.linspace(0, 10 * np.pi, N)
    r = theta**2
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

x, y = Galilean_spiral(1000)
f2 = plt.figure(2)
plt.title("Galilean Spiral")
plt.plot(x, y)

# Part C
def Fey(N):
    theta = np.linspace(0, 24 * np.pi, N)
    r = np.exp(np.cos(theta)) - 2 * np.cos(4 * theta) + (np.sin(theta/12.0))**5
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

x, y = Fey(1000)
f3 = plt.figure(3)
plt.title("Fey's function")
plt.plot(x, y)

plt.show()



