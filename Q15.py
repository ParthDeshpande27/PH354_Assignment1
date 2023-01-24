# Exercise 15: Scanning Tunneling Microscope

import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt(r"stm.txt")

plt.imshow(x, extent=[-x.shape[1]/2., x.shape[1]/2., -x.shape[0]/2., x.shape[0]/2. ])
plt.title("STM image of Silicon")
plt.show()
    

