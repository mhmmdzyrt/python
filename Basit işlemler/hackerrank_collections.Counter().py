from collections import Counter

n = int(input())
shoe_list = Counter(list(map(int, input().split())))
money_earned = 0
for _ in range(int(input())):
    order = list(map(int, input().split()))
    if shoe_list[order[0]] > 0:
        shoe_list[order[0]] -= 1
        money_earned += order[1]
    if shoe_list[order[0]] == 0:
        continue
print(money_earned)