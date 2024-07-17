stacks = [['F','G','V','R','J','L','D'], 
['S','J','H','V','B','M','P','T'], 
['C','P','G','D','F','M','H','V'],
['Q','G','N','P','D','M'],
['F','N','H','L','J'],
['Z','T','G','D','Q','V','F','N'],
['L','B','D','F'],
['N','D','V','S','B','J','M'],
['D','L','G']]

lines = []

with open("input5.txt", "r") as file:
    for line in file:
        instance = []
        line = line.strip()
        i = 0
        while i < len(line):
            if (i != len(line) - 1) and line[i].isdigit() and line[i + 1].isdigit():
                instance.append(int(line[i] + line[i + 1], base = 10))
                i += 1
            elif line[i].isdigit():
                instance.append(int(line[i], base = 10))  
            i += 1     
        lines.append(instance)

i = 0
while i < len(lines):      
    numMoves = lines[i][0]
    moveFrom = stacks[lines[i][1] - 1]
    moveTo = stacks[lines[i][2] - 1]
    for k in range(numMoves):
        moveTo.insert(0, moveFrom[numMoves - k - 1])
        moveFrom.pop(numMoves - k - 1)
    i += 1

print(stacks)
for i in range(len(stacks)):
    if i != len(stacks) - 1:
        print(stacks[i][0], end = '')
    else:
        print(stacks[i][0])
