import numpy

N, M, P = map(int, input().split())
arr_1 = []
arr_2 = []
for _ in range(N):
    arr_1.append(list(map(int, input().split())))
for _ in range(M):
    arr_2.append(list(map(int, input().split())))
arr_1 = numpy.array(arr_1)
arr_2 = numpy.array(arr_2)

print(numpy.concatenate((arr_1, arr_2), axis=0))