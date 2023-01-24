# Exercise 2: Altitude of a satellite
# A satellite is to be launched into a circular orbit around the Earth so that it
# orbits the planet once every T seconds.
# a) Write a program that asks the user to enter the desired value of T and
# then calculates and prints out the correct altitude of the satellite above the
# Earth’s surface in meters.
# b) Use your program to calculate the altitudes of satellites that orbit the Earth
# once a day (so-called “geosynchronous” orbit), once every 90 minutes, and
# once every 45 minutes. What do you conclude from the last of these calculations?
# c) Technically a geosynchronous satellite is one that orbits the Earth once per
# sidereal day, which is 23.93 hours, not 24 hours. Why is this? And how
# much difference will it make to the altitude of the satellite?

import math
import numpy

# Part A

time = input("Enter the time period (T) of satellite in seconds: ")
# Earth's mean radius in metres (Re)
Re = 6378100
# Earth's mass in kilograms (Me)
Me = 5.972e+24
# The Gravitational constant G in SI units
G = 6.674e-11
height = numpy.cbrt(((float(time)/(2*math.pi))**2)*G*Me) - Re
print("Altitude of the satellite above the Earth’s surface in meters: " + str(round(height)))

# Part B

height24h = (height + Re)*(float(time)/(24*60*60)) - Re
print("Altitude of a geosynchronous satellite (i.e., T = 24 hours) above the Earth’s surface in meters: " + str(round(height24h)))
height90min = (height + Re)*(float(time)/(90*60)) - Re
print("Altitude of a satellite (with T = 90 minutes) above the Earth’s surface in meters: " + str(round(height90min)))
height45min = (height + Re)*(float(time)/(45*60)) - Re
print("Altitude of a satellite (with T = 45 minutes) above the Earth’s surface in meters: " + str(round(height45min)))
