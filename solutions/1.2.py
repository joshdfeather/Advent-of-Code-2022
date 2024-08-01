
file = open('input1.txt', 'rt');
lines = file.readlines()

current = []
elves = []

for line in lines:
    if line == '\n':
        elves.append(current)
        current = []
    else: 
        current.append(line.strip("\n"))

maxs = []
total = 0;

for elf in elves:
    counter = 0
    for value in elf:
        counter += int(value)
    maxs.append(counter);

maxs.sort()

for i in range(3):
    total += maxs[-(i + 1)]

print(total)
file.close()