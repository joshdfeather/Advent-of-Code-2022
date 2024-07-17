
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

max = 0;
for elf in elves:
    counter = 0
    for value in elf:
        counter += int(value)
    if counter > max:
         max = counter

print(max)
file.close()