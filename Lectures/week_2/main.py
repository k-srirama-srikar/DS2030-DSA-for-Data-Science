from algo import *
import sys
import time
import random

def rand_list(n):
    return [random.randint(0,1000) for _ in range(n)]

i_times = []
m_times = []

for n in range(1,1001):
    print(n)
    ni_times = []
    mi_times = []
    for _ in range(20):
        arri = rand_list(n)
        arrm = arri[::]
        ts = time.time()
        insertionSort(arri)
        te = time.time()
        ni_times.append(te-ts)
        ts=time.time()
        mergeSort(arrm, 0, len(arrm)-1)
        te=time.time()
        mi_times.append(te-ts)
    i_times.append((n, sum(ni_times)/20))
    m_times.append((n, sum(mi_times)/20))

with open('insertion_times.data', 'w') as file:
    for i in i_times:
        file.write(str(i[0]) + ' ' + str(i[1]) + '\n')

with open('merge_times.data', 'w') as file:
    for i in m_times:
        file.write(str(i[0]) + ' ' + str(i[1]) + '\n')


