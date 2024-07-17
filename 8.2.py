## 99 x 99 grid

import time
lines = []
counter = 0
vals = []

with open("input8.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

for i in range(99):
    for j in range(99):
        list = [0, 0, 0, 0]
        r = 99 - j - 1
        l = j
        u = i
        d = 99 - i - 1
        val = lines[i][j]
        for a in range(r):
            if lines[i][j + a + 1] < val:
                list[0] += 1
            else:
                list[0] += 1
                break
        for b in range(l):
            if lines[i][j - b - 1] < val:
                list[1] += 1
            else:
                list[1] += 1
                break
        for c in range(u):
            if lines[i - c - 1][j] < val:
                list[2] +=1
            else:
                list[2] += 1
                break
        for e in range(d):
            if lines[i + e + 1][j] < val:
                list[3] += 1
            else:
                list[3] += 1
                break
        output = list[0] * list[1] * list[2] * list[3]
        vals.append(output)

print(max(vals))