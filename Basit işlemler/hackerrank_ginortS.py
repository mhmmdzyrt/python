sorted_string = sorted(input())
string_number = []
string_upper = []
string_lower = []
for char in sorted_string:
    if char.isdigit() and int(char) % 2 == 1:
        string_number.append(char)
for char in sorted_string:
    if char.isdigit() and int(char) % 2 == 0:
        string_number.append(char)
    if char.islower():
        string_lower.append(char)
    if char.isupper():
        string_upper.append(char)

print(*(string_lower + string_upper + string_number), sep='')
# print(''.join((string_lower + string_upper + string_number)))
