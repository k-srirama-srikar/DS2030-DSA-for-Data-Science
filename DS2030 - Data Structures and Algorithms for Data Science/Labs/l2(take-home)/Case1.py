from steps import *
# importing the frcursive function from steps.py
import sys

syar = sys.argv
# we'll be taking input form the user, when the program is to be executed
l1 = [int(x) for x in syar[1:]]
# we then make a proper list of the given arguments 
grid = [[0]*l1[0] for _ in range(l1[0])]
# makig a grid matrix although it wasn't used
n = l1[0]
# dimension of the given grid
position = (l1[1], l1[2])
# start position
station  = (1,1)
# position of charging station or rather the end position
print(steps(position, station))
# printing the return value of function