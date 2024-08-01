info = []

with open("input10.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line[-1].isdigit():
            inst, val = line.split()
            info.append((inst, int(val)))
        else:
            info.append(("noop", 0))

X = 1
cycle = 0
Cycles = {i:1 for i in range(1,241)}

for line in info:
    cycle += 1
    Cycles[cycle] = X
    if line[0] == "addx":
        cycle += 1
        Cycles[cycle] = X
        X += line[1]

part1 = 0
for i in range(20, 221, 40):
    part1 += i * Cycles[i]

print("\n", end = '')
print(f'Part 1: {part1}')
print("\n", end = '')
print("Part 2: ")
print("\n", end = '')

position = 0
xcord = 0
for i in range(240):
    position += 1
    if Cycles[position] - 1 <= xcord <= Cycles[position] + 1:
        print("#", end = '')
    else:
        print(" ", end = '')
    xcord += 1
    if position in [40, 80, 120, 160, 200, 240]:
        print("\n", end = '')
        xcord = 0
print("\n", end = '')
