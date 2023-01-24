# Exercise 6: Planetary orbits
# The orbit in space of one body around another, such as a planet around the Sun,
# need not be circular. In general, it takes the form of an ellipse, with the body
# sometimes closer in and sometimes further out. If you are given the distance ℓ1
# of the closest approach that a planet makes to the Sun, also called its perihelion, and
# its linear velocity v1 at perihelion, then any other property of the orbit can be
# calculated from these two. Kepler’s second law tells us that the distance ℓ2 and
# velocity v2 of the planet at its most distant point, or aphelion, satisfy ℓ2v2 = ℓ1v1.
# Write a program that asks the user to enter the distance to the Sun and velocity
# at perihelion, then calculates and prints the quantities ℓ2, v2, Orbital period T,
# and Orbital eccentricity e.
# Test your program by having it calculate the properties of the orbits of the
# Earth (for which ℓ1 = 1.4710×1011 m and v1 = 3.0287×104 m s−1
# ) and Halley’s
# comet (ℓ1 = 8.7830 × 1010 m and v1 = 5.4529 × 104 m s−1
# ). Among other things,
# you should find that the orbital period of the Earth is one year and that of
# Halley’s comet is about 76 years.


import math

l1 = float(input("Enter the perihelion distance in meters: "))
v1 = float(input("Enter the perihelion velocity in meters per second: "))
# mu is the heliocentric gravitational parameter mu = GM in SI units
mu = 1.32712440042e20

a = (2/l1 - (v1**2)/mu)**(-1)
eccentricity = 1 - l1/a
l2 = a*(1+eccentricity)
v2 = l1*v1/l2
T = 2*math.pi*math.sqrt(a**3/mu)
print("\nFor the heliocentric user-defined system:")
print("The aphelion distance in metres is: " + str(round(l2, 8)))
print("The aphelion velocity in metres per second is: " + str(round(v2, 8)))
print("The orbital time period in seconds is: " + str(round(T, 8)))
print("The orbital eccentricity is: " + str(round(eccentricity, 8)))
print("\n")

l1 = 1.471e11
v1 = 3.0287e4
a = (2/l1 - (v1**2)/mu)**(-1)
eccentricity = 1 - l1/a
l2 = a*(1+eccentricity)
v2 = l1*v1/l2
T = 2*math.pi*math.sqrt(a**3/mu)
print("For the Earth:")
print("The aphelion distance in metres is: " + str(round(l2, 8)))
print("The aphelion velocity in metres per second is: " + str(round(v2, 8)))
print("The orbital time period in seconds is: " + str(round(T, 8)))
print("The orbital eccentricity is: " + str(round(eccentricity, 8)))
print("\n")

l1 = 8.783e10
v1 = 5.4529e4
a = (2/l1 - (v1**2)/mu)**(-1)
eccentricity = 1 - l1/a
l2 = a*(1+eccentricity)
v2 = l1*v1/l2
T = 2*math.pi*math.sqrt(a**3/mu)
print("For Halley's comet:")
print("The aphelion distance in metres is: " + str(round(l2, 8)))
print("The aphelion velocity in metres per second is: " + str(round(v2, 8)))
print("The orbital time period in seconds is: " + str(round(T, 8)))
print("The orbital eccentricity is: " + str(round(eccentricity, 8)))
print("\n")



