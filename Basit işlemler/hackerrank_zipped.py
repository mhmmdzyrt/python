n, m = map(int, input().split())
k = []
for _ in range(m):
    k.append(map(float, input().split()))
for i in zip(*k):
    print(sum(i) / m)