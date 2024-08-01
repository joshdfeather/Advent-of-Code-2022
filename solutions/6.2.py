
lines = []

with open('input6.txt', 'r') as file:
    lines = [line.strip() for line in file]

for line in lines:
    for i in range(len(line) - 13):
        values = set()
        j = i
        while j < i + 14:
            values.add(line[j])
            j += 1
        if len(values) == 14:
            print(i + 14)
            print(values)
            break