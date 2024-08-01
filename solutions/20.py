
with open("input20.txt", "r") as file:
    lines = [(i, line.strip()) for i, line in enumerate(file)]

SEEN = set()
length = len(lines)

while len(SEEN) != len(lines):
    for (i, val) in lines:
        if (i, val) in SEEN:
            continue
        SEEN.add((i, val))
        x = int(val)
        if x < 0:
            while x < 0:
                x = length + x - 1
        new = (lines.index((i, val)) + x)
        if new == length:
            new = 0
        if new > length:
            while new > length:
                new = new - length + 1        
                if new == length:
                    new = 0
        lines.remove((i, val))
        lines.insert(new, (i, val))
        if new > i:
            break

counter = 0
for (i, val) in lines:
    if val == '0':
        counter = lines.index((i, val))
print(counter)

y = 0
j = 0
while (j <= counter + 4000):
    for (i, val) in lines:
        if j == counter + 1000 or j == counter + 2000 or j == counter + 2998:
            print(j, val)
            y += int(val) 
        j += 1 
print(y)





