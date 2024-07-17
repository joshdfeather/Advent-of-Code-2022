
with open("input18.txt", "r") as file:
    lines = [line.strip() for line in file]

centres = []
for line in lines:  
    x, y, z = line.split(',')
    centres.append((int(x), int(y), int(z)))

adjacents = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

count = 0
for x, y, z in centres:
    for dx, dy, dz in adjacents:
        nx = x + dx
        ny = y + dy
        nz = z + dz
        if not (nx, ny, nz) in centres:
            count += 1
            
print(f'Part 1: {count}')

from collections import deque
counter = 0
stack = deque([(0, 0, 0)])
seen = set()
while stack:
    x, y, z = stack.popleft()
    if (x > 22 or x < -1 or y > 22 or y < -1 or z > 22 or z < -1):
        continue
    if (x, y, z) in seen:
        continue
    seen.add((x, y, z))
    for dx, dy, dz in adjacents:
        nx, ny, nz = x + dx, y + dy, z + dz
        if (nx, ny, nz) in centres:
            counter += 1
        else:
            stack.append((nx, ny, nz))

print(f'Part 2: {counter}')