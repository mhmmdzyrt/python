# python

import numpy
N, M = list(map(int, input().split()))
arr = []  # python
for _ in range(N):
    arr.append(list(map(int, input().split())))  # python

my_array = numpy.array(arr)
print(numpy.transpose(my_array))  # python
print(my_array.flatten())
