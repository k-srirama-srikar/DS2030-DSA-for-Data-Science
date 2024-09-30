import sys
from steps import *

syar = sys.argv
l1 = [int(x) for x in syar[1:]]
grid = [[0]*l1[0] for _ in range(l1[0])]
n = l1[0]
pos = (l1[1], l1[2])
st = (l1[3], l1[4])

# conditional to check if values given are apt 
if l1[1]>n or l1[2]>n or l1[3]>n or l1[4]>n:
    print("ERROR: Position not in the grid!!")
    sys.exit()

# everyting until here is almost the same as that of Case1.py
# with the exception of the new variable used here, st,
s = 0
# a variable to store the function return value
if pos[0] > st[0] and pos[1]>st[1]:
    s = steps(pos, st)
    # to chack if it's similar to the case as that of case 1
elif pos[0]>st[0]:
    s = steps((pos[0], n-pos[1]+1), (st[1], n-st[1]+1))
    # we basically convert the given cordinates into coordinates suitable for the recursive function
    # rather we just rotate the matrix in such a fashion so that, the values of the position and the 
    # chargaing station fit the requirements of the recursive function
elif pos[1]>st[1]:
    s = steps((n-pos[0]+1, pos[1]), (n-st[0]+1, st[1]))
else:
    s = steps((n-pos[0]+1,n-pos[1]+1), (n-st[0]+1,n-st[1]+1))

print(s)