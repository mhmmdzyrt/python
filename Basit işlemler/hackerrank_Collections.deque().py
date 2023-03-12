from collections import deque
d = deque()

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == 'append':
        d.append(int(cmd[1]))
    if cmd[0] == 'appendleft':
        d.appendleft(cmd[1])
    if cmd[0] == 'pop':
        d.pop()
    if cmd[0] == 'popleft':
        d.popleft()
print(*d)