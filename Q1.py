# Exercise 1: A ball dropped from a tower
# A ball is dropped from a tower of height h with initial velocity zero. Write a
# program that asks the user to enter the height in meters of the tower and then
# calculates and prints the time the ball takes until it hits the ground, ignoring
# air resistance. Use your program to calculate the time for a ball dropped from
# a 100 m high tower.
import math

height = input("Enter the height in meters: ")
gacc = 9.8
time = math.sqrt(2*float(height)/gacc)
print("The time taken to hit the ground in seconds: " + str(round(time, 3)))
time100 = math.sqrt(2*100/gacc)
print("The time taken to hit the ground in seconds for a height of 100 metres: " + str(round(time100, 3)))