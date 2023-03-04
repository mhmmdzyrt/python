from itertools import product

K, N = map(int, input().split())
list_1 = list()
for i in range(K):
    list_1.append(list(map(int, input().split()))[1:])
ans = []
for i in list(product(*list_1)):
    x = 0
    for j in i:
        x += j ** 2
    ans.append(x % N)
print(max(ans))
