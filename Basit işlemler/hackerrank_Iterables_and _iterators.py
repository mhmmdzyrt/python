from itertools import combinations
len_string = int(input())
string = input().split()
split_string = int(input())
comb_list = list(combinations(string, split_string))
count = 0
for i in comb_list:
    for j in i:
        if j == 'a':
            count += 1
            break
print('{:.4f}'.format(count/len(comb_list)))