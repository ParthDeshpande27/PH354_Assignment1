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
import numpy as np

# Part A

time = float(input("Enter the time period (T) of satellite in seconds: "))
# Earth's mean radius in metres (Re)
Re = 6.3781e6
# Earth's mass in kilograms (Me)
Me = 5.972e+24
# The Gravitational constant G in SI units
G = 6.674e-11

def heightfromtime(time):
    height = (G * Me * (time / (2 * math.pi)) ** 2) ** (1/3) - Re
    return height

print("Altitude of the satellite above the Earth’s surface in meters: " + str(round(heightfromtime(time), 2)))

# Part B

print("Altitude of a geosynchronous satellite (i.e., T = 24 hours) above the Earth’s surface in meters: " + str(round(heightfromtime(24*60*60), 2)))
print("Altitude of a satellite (with T = 90 minutes) above the Earth’s surface in meters: " + str(round(heightfromtime(90*60), 2)))
print("Altitude of a satellite (with T = 45 minutes) above the Earth’s surface in meters: " + str(round(heightfromtime(45*60), 2)))

# This calculation shows that the height is negative
# (i.e., the satellite would have to travel through the ground, which is impossible)
# This implies that there exists a minimum time period of the satellite (around 85 minutes)

# Part C

# Technically a geosynchronous satellite is one that orbits the Earth once per
# sidereal day, which is 23.93 hours, not 24 hours. Why is this?

# ANSWER:
# The earth is rotating and also revolving around the sun in an approximately circular orbit.
# If the earth were not revolving around the sun, the sidereal day would equate a day in the normal sense of the word.
# However, as the earth rotates once, it has moved some distance around the sun, i.e., relative to the Earth,
# the Sun has moved some distance.
# This implies that the time period of sun rise will not be equal to the sidereal day (a normal day happens
# to be slightly longer i.e., 24 hours as compared to a sidereal day of 23.93 hours)
# For calculation of the sidereal day, we refer to very distant stars so that the relative angular displacement
# is negligible.

print("Altitude of a sidereal geosynchronous satellite (i.e., T = 23.93 hours) ")
print("above the Earth’s surface in meters: " + str(round(heightfromtime(23.93*60*60), 2)))
print("The difference in metres is: ")
print(round(heightfromtime(24*60*60) - heightfromtime(23.93*60*60), 2))

# i.e., the difference is around 82 km, negligible compared to 36000 km.