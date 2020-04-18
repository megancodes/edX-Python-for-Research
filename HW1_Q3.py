# Exercise 3
# A list of numbers representing measurements obtained from a system of interest can often be noisy.
# One way to deal with noise to smoothen the values by replacing each value with the average of the value
# and the values of its neighbors.

#3a

#Let's make a function moving_window_average(x, n_neighbors) that takes a list x and the number of neighbors
# n_neighbors on either side to consider. For each value, the function computes the average of each value's
#neighbors, including themselves. Have the function return a list of these averaged values that is the same
#length as the original list. If there are not enough neighbors (for cases near the edge), substitute the
#original value as many times as there are missing neighbors.
#Use your function to find the moving window sum of x=[0,10,5,3,1,5] and n_neighbors=1.
import random
random.seed(1)

def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    return [sum(x[i:i+width]) / width for i in range(n)]

x = [0,10,5,3,1,5]
print(moving_window_average(x, 1))

#3b
#Compute and store R=1000 random values from 0-1 as x.
#Compute the moving window average for x for the range of n_neighbors 1-9.
#Store x as well as each of these averages as consecutive lists in a list called Y.

random.seed(1)

R = 1000
x = [random.uniform(0,1) for i in range(R)]
Y = [x] + [moving_window_average(x, n_neighbors) for n_neighbors in range(10)]
print(len(Y))

#3c
#For each list in Y, calculate and store the range (the maximum minus the minimum) in a new list ranges.
#Print your answer. As the window width increases, does the range of each list increase or decrease?
#Why do you think that is?

ranges = [max(x)-min(x) for x in Y]
print(ranges)
#The range decreases, because the average smooths a larger number of neighbors.