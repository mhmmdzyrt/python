from collections import OrderedDict
order_dict = OrderedDict()

for _ in range(int(input())):
    items = input().split()
    item_names = ' '.join(items[:-1])
    if item_names in order_dict:
        order_dict[item_names] += int(items[-1])
    else:
        order_dict[item_names] = int(items[-1])

for i in order_dict.items():
    print(*i)
