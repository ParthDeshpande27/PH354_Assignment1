# Exercise 8: The Madelung constant
# The write-up is too big to fit here.

import math

N = 300
M = 0

# Calculation was done using Benson's formula (as on Wikipedia) since it converges faster

for n in range(1, N, 2):
    for m in range(n, N, 2):
        if n == m:
            multiplicity = 1
        else:
            multiplicity = 2
        M += multiplicity * math.cosh(0.5*math.pi*math.hypot(n, m))**(-2)
M = 12*math.pi*M

print("The value of the Madelung constant for NaCl is: " + str(M))

