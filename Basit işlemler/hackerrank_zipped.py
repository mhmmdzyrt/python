# python

n, m = map(int, input().split())  # python
k = []
for _ in range(m):
    k.append(map(float, input().split()))  # python
for i in zip(*k):
    print(sum(i) / m)
