alphabet = 'abcdefghijklmnopqrstuvwxyz'

x = 9  # 0 < x < 27

list_1 = []  # c b a
for i in alphabet[:x][::-1]:
    list_1.append(i)
list_1.extend(list_1[:-1][::-1])
len_list = len(list_1)
string = ''
for i in list_1:
    string += i
end_list = list()
while True:
    if len(list_1) == 1:
        # print('-'.join(list_1).center(len_list*2, '-'))
        end_list.append('-'.join(list_1).center(len_list*2-1, '-'))
        break
    # print('-'.join(list_1).center(len_list*2, '-'))
    end_list.append('-'.join(list_1).center(len_list*2-1, '-'))
    list_1.pop(len(list_1) // 2)
    list_1.pop(len(list_1) // 2 - 1)
for i in end_list[::-1]:
    print(i)
for i in end_list[1:]:
    print(i)