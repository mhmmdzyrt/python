# 3 lines of code
m, number_list = int(input()), list(map(int, input().split()))
number_polid, number_postive = [0 < i == int(str(i)[::-1]) for i in number_list], [i > 0 for i in number_list]
[print(True) if all(number_postive) and any(number_polid) else print(False) for i in range(1)]