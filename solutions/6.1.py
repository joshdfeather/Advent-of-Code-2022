import time
lines = []


with open('input6.txt', 'r') as file:
    for line in file:
        lines.append(line)

for line in lines:
    for i in range(len(line) - 3):
        values = set()
        j = i
        while j < i + 4:
            values.add(line[j])
            j += 1
        if len(values) == 4:
            print(i + 4)
            print(values)
            break