# Exercise 7: Catalan numbers
# The Catalan numbers Cn are a sequence of integers 1, 1, 2, 5, 14, 42, 132. . . that
# play an important role in quantum mechanics and the theory of disordered systems.
# (They were central to Eugene Wigner’s proof of the so-called semicircle
# law.) They are given by
# C0 = 1
# Cn+1 = (4n + 2)/(n + 2)Cn
# Write a program that prints in increasing order all Catalan numbers less than
# or equal to one billion.

import math
print("Here follow the first few Catalan numbers less than or equal to a billion:")
Catalan = [1, 0]

while Catalan[0] <= 1e9:
    print(str(int(Catalan[1])+1) + " " + str(int(Catalan[0])))
    Catalan[0] = ((4*Catalan[1] + 2)/(Catalan[1]+2))*Catalan[0]
    Catalan[1] = Catalan[1]+1

