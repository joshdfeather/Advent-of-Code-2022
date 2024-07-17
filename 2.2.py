
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
    max += (val2 - 1) * 3
    if (val1 == 3) and (val2 == 3):
        max += 1
    elif (val1 == 1 and val2 == 1):
        max += 3
    elif (val2 == 3):
        max += val1 + 1
    elif (val2 == 2):
        max += val1
    elif (val2 == 1):
        max += val1 - 1

print(max)