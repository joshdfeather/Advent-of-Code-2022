
lines = []

val1s = ['A', 'B', 'C']
val2s = ['X', 'Y', 'Z']

with open('input2.txt', 'r') as file:
    for line in file:
        lines.append(line.strip())

max = 0
val = 0

for line in lines:

    val2 = val2s.index(line[-1]) + 1
    val1 = val1s.index(line[0]) + 1
    max += val2
    if (val2 == 1 and val1 == 3):
        max += 6
    elif val2 == val1 + 1:
        max += 6
    elif val2 == val1:
        max += 3

print(max)