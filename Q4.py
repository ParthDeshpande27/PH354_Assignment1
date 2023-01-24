# Exercise 4: A spaceship travels from Earth in a straight line at relativistic speed v
# to another planet x light years away. Write a program to ask the user for the
# value of x and the speed v as a fraction of the speed of light c, then print out
# the time in years that the spaceship takes to reach its destination (a) in the rest
# frame of an observer on Earth and (b) as perceived by a passenger on board
# the ship. Use your program to calculate the answers for a planet 10 light years
# away with v = 0.99c.
import math

x = float(input("Enter the distance to the planet in light years: "))
v = float(input("Enter the speed of the spaceship as a fraction of the speed of light (c) : "))
c = 2.99792458e8
gamma = 1.0/math.sqrt(1-v**2)
timeEarth = x/v

# Part A
print("The time in years that the spaceship takes to reach its destination as from Earth: " + str(round(timeEarth, 3)))

# Part B
timePassenger = timeEarth/gamma
print("The time in years that the spaceship takes to reach its destination as by a passenger: " + str(round(timePassenger, 3)))