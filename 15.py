import time
start = time.time()
with open("input15.txt", "r") as file:
    lines = [line.strip() for line in file]

S = set()
B = set()
for line in lines:
    words = line.split()
    sx,sy = words[2],words[3]
    bx,by = words[8],words[9]
    sx = int(sx[2:-1])
    sy = int(sy[2:-1])
    bx = int(bx[2:-1])
    by = int(by[2:])
    d = abs(sx - bx) + abs(sy - by)
    S.add((sx,sy,d))
    B.add((bx,by))

S = frozenset(S)

def valid(x,y,S):
    for (sx,sy,d) in S:
        dxy = abs(x - sx) + abs(y - sy)
        if dxy <= d:
            return False
    return True

p1 = 0
for x in range(-int(5e6),int(5e6)):
    y = int(2e6)
    if not valid(x,y,S) and (x, y) not in B:
        p1 += 1

print(f'Part 1: {p1}')
print(time.time() - start)