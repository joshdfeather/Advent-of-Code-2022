
pairs = []
with open("input13.txt", "r") as file:
    lines = [line for line in file]
    for i in range(len(lines)):
        if lines[i] == '\n':
            pairs.append((lines[i - 2].strip(), lines[i - 1].strip()))
    pairs.append((lines[- 2].strip(), lines[- 1].strip()))

def compare(L, R):
    if isinstance(L, int) and isinstance(R, int):
        if L < R: 
            return -1
        elif L > R:
            return 1
        else:
            return 0
    elif isinstance(L, list) and isinstance(R, list):
        i = 0
        while i < len(L) and i < len(R):
            c = compare(L[i], R[i])
            if c == 1:
                return 1
            elif c == -1:
                return -1
            i += 1
        if i == len(L) and i < len(R):
            return -1
        elif i < len(L) and i == len(R):
            return 1
        else:
            return 0
    elif isinstance(L, list) and isinstance(R, int):
        return compare(L, [R])
    else:
        return compare([L], R)

indexes = 0
for j in range(len(pairs)):
    L = eval(pairs[j][0])
    R = eval(pairs[j][1])
    if compare(L, R) != 1:
        indexes += j + 1

print(f'Part 1: {indexes}')

from functools import cmp_to_key
packets = []
for line in lines:
    if line != '\n':
        packets.append(eval(line.strip()))
packets.append([[2]])
packets.append([[6]])
packets = sorted(packets, key = cmp_to_key(lambda L,R: compare(L, R)))

index1 = 0
index2 = 0
for i in range(len(packets)):
    if packets[i] == [[2]]:
        index1 = i + 1
    elif packets[i] == [[6]]:
        index2 = i + 1

print(f'Part 2: {index1 * index2}')
