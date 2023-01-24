# Exercise 3: Write a program to ask the user for the Cartesian coordinates x, y
# of a point in two-dimensional space, and calculate and print the corresponding
# polar coordinates, with the angle θ given in degrees.
import math
import numpy

x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))
r = math.sqrt(x**2+y**2)
theta = numpy.degrees(math.atan2(y,x))
print("The corresponding radial coordinate is: " + str(round(r, 5)))
print("The corresponding angular coordinate in degrees is: " + str(round(theta, 3)))