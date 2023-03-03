def check(string):
    end_string = ''
    char = '#0123456789ABCDEFabcdef'
    for i, j in enumerate(string):
        if j != '{':
            continue
        else:
            for i in string[i:]:
                # print(i, end='')
                end_string += i
                if i == '}':
                    break
        # print(i)
        end_string += i
    end_index = ''
    for i, j in enumerate(end_string):
        if j == '#':
            for index in end_string[i:i + 7]:
                if index in char:
                    end_index += index
            if len(end_index) == 4 or len(end_index) == 7:
                print(end_index)
            end_index = ''


code_list = []
text = ''
for _ in range(int(input())):
    code_list.append(input())

for i in code_list:
    text += i

check(text)
