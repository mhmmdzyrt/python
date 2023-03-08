import math
import os
import random
import re
import sys


def location(list1):
    return list1[k]


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().split())))
    k = int(input())
    arr.sort(key=location)
    for i in arr:
        print(*i)