# Exercise 2
#The ratio of the areas of a circle and the square inscribing it is pi / 4.
#In this six-part exercise, we will find a way to approximate this value.

#2a
#Using the math library, calculate and print the value of pi / 4.
import math

print(math.pi / 4)

#2b
#Using random.uniform, create a function rand() that generates a single float between -1 and 1.
#Call rand() once. So we can check your solution, we will use random.seed to fix the value called
#by your function.
import random
random.seed(1) # Fixes the seed of the random number generator

def rand():
    return random.uniform(-1, 1)

print(rand())

#2c
#The distance between two points x and y is the square root of the sum of squared differences along
#each dimension of x and y. Create a function distance(x, y) that takes two vectors and outputs the
#distance between them. Use your function to find the distance between (0,0) and (1,1).
#Print your answer.
def distance(x, y):
    return math.sqrt((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2)

print(distance((0,0), (1,1)))

#2d
#distance(x, y) is pre-loaded from part 2c. Make a function in_circle(x, origin) that uses distance
#to determine if a two-dimensional point falls within the the unit circle with a given origin.
#That is, find if a two-dimensional point has distance <1 from the origin (0,0).
#Use your function to print whether the point (1,1) lies within the unit circle centered at (0,0).

def in_circle(x, origin = (0,0)):
    return distance(x, origin) < 1

print(in_circle((1,1)))

#2e
#The functions rand and in_circle are defined from previous exercises.
#Using these functions, code is pre-entered that creates a list x of R=10000
#two-dimensional points. Create a list of 10000 booleans called inside that are
#True if and only if the point in x with that index falls within the unit circle.
#Make sure to use in_circle!
#Print the proportion of points within the circle.
#This proportion is an estimate of the ratio of the two areas!

R = 10000
x = [ (rand(), rand()) for i in range(R)] #list comprehension
inside = [ in_circle(j) for j in x]
print(sum(inside)/ R)

#2f
#Note: inside and R are defined as in Exercise 2e. Recall the true ratio of the area of of the unit circle
#to the area to the inscribing square is pi / 4.
#Find and print the difference between this value and your estimate from part 2e.
print((math.pi / 4) - (sum(inside)/R))
