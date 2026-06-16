# python

from itertools import combinations

s = list(input().split())

for _ in range(1, int(s[1]) + 1):
    comb_list = list(combinations(s[0], _))  # python
    sorted_list = []
    for i in comb_list:
        sorted_list.append(''.join(sorted(i)))  # python
    sorted_list.sort()
    [print(i) for i in sorted_list]
