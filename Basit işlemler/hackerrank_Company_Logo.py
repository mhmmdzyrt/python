def check(sequence):
    return sequence[1]


if __name__ == '__main__':
    s = sorted(input())
    s_set = list(set(s))
    s_set.sort()
    count = dict()

    for i in s_set:
        count[i] = s.count(i)

    k = list(count.items())
    k.sort(reverse=True, key=check)
    for sort in k[:3]:
        print(*sort)
