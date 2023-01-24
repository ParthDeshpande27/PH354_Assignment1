# Exercise 16: Deterministic Chaos

import numpy as np
import matplotlib.pyplot as plt

r_val = np.arange(start=0, stop=4, step=0.0001)

f1 = plt.figure(1)
x = np.full_like(r_val, 0.5)
for i in range(1, 2001):
    x = r_val * (1 - x) * x
    if i >= 1000:
        plt.scatter(r_val, x, 0.04)

plt.ylabel("x")
plt.xlabel("r")
plt.title("Feigenbaum plot")
plt.show()

# Note for x = 0.5, the graph always went into the lower branch at the first branching point
# To generate the full-tree, x was randomly sampled from 0 to 1 in 100 trials.
# Different colors represent different trials in the outermost loop


# Part A and B

def XRplotgen(x, r):
    iteration = np.linspace(1, 100, 100)
    x_val = np.full_like(iteration, 0.5)
    x_val[0] = x
    for idx in range(len(iteration)):
        if idx+1 >= len(iteration):
            break
        x_val[idx+1] = r * (1 - x_val[idx]) * x_val[idx]
    f2 = plt.figure(2)
    plt.plot(iteration, x_val)

#XRplotgen(0.7, 2)
#XRplotgen(0.7, 3)
XRplotgen(0.7, 3.8)

# Uncomment 1st line to see fixed point, 2nd for a bistable limit cycle

plt.show()

# ANSWERS
# The edge of chaos seems to be around r = 3.57