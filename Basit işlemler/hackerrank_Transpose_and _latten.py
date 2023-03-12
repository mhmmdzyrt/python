import numpy
N, M = list(map(int, input().split()))
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

my_array = numpy.array(arr)
print(numpy.transpose(my_array))
print(my_array.flatten())