# Exercise 5: Quantum potential step
# A well-known quantum mechanics problem involves a particle of mass m that
# encounters a one-dimensional potential step (refer to the pdf for diagram).
# The particle with initial kinetic energy E and wavevector k1 = √2mE/hcross enters
# from the left and encounters a sudden jump in potential energy of height V
# at position x = 0. By solving the Schrodinger equation, one can show that when E > V
# the particle may either (a) pass the step, in which case it has a
# lower kinetic energy of E − V on the other side and a correspondingly smaller
# wavevector of k2 = sqrt(2m(E − V))/hcross, or (b) it may be reflected, keeping all of
# its kinetic energy and an unchanged wavevector but moving in the opposite
# direction.
# Suppose we have a particle with mass equal to the electron mass m = 9.11e−31 kg
# and energy 10 eV encountering a potential step of height 9 eV. Write
# a Python program to compute and print out the transmission and reflection
# probabilities.

import math
import cmath

E = float(input("Enter the energy of the particle in eV: "))
V = float(input("Enter the potential barrier in eV: "))
# The final probabilities depend only on the ratios of k (i.e., mass, hcross, etc. don't matter)
k1 = math.sqrt(E)
k2 = cmath.sqrt(E-V)
r = (k2-k1)/(k2+k1)
R = abs(r)**2
print("The reflection probability is: " + str(round(R, 8)))
print("The transmission probability is: " + str(round(1-R, 8)))