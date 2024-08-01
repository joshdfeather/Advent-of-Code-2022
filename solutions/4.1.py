
pairs = []

int1 = 0
int2 = 0
int3 = 0
int4 = 0

max = 0

with open("input4.txt", "r") as file:
    for line in file:
        pairs.append(line.strip().split(','))

for pair in pairs:
    for i in range(len(pair[0])):
        if pair[0][i] == '-':
            int1 = int(pair[0][:i])
            int2 = int(pair[0][i + 1:])
    for j in range(len(pair[1])):
        if pair[1][j] == '-':
            int3 = int(pair[1][:j])
            int4 = int(pair[1][j + 1:])
    if (int4 >= int2 and int3 <= int1) or (int1 <= int3 and int2 >= int4):
        max += 1
       
print(max)