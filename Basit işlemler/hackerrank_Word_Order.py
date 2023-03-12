import collections

string_list = []
for _ in range(int(input())):
    string_list.append(input())

print(len(set(string_list)))
counter_dict = dict(collections.Counter(string_list))

for i in counter_dict.values():
    print(i, end=' ')