
info = []
tailpositions = set()
with open("input9.txt", "r") as file:
    for line in file:
        line = line.strip()
        mov,val = line.split(" ")
        info.append((mov, int(val)))

head = knot1 = knot2 = knot3 = knot4 = knot5 = knot6 = knot7 = knot8 = tail = (0, 0)

def check(head, tail, letter):
    dh = head[0] - tail[0]
    dv = head[1] - tail[1]
    if abs(dh) == abs(dv) == 1:
        pass
    elif abs(dh) == 2 and abs(dv) == 0:
        tail = (tail[0] + 1, tail[1])
        if dh < 0:
            tail = (tail[0] - 2, tail[1])
    elif abs(dh) == 0 and abs(dv) == 2:
        tail = (tail[0], tail[1] + 1)
        if dv < 0:
            tail = (tail[0], tail[1] - 2)
    elif dh > 0 and dv > 0:
        tail = (tail[0] + 1, tail[1] + 1)
    elif dh > 0 and dv < 0:
        tail = (tail[0] + 1, tail[1] - 1)
    elif dh < 0 and dv > 0:
        tail = (tail[0] - 1, tail[1] + 1)
    elif dh < 0 and dv < 0:
        tail = (tail[0] - 1, tail[1] - 1)
    if letter == 'Y':
        tailpositions.add(tail)
    return tail


def run(head, knot1, knot2, knot3, knot4, knot5, knot6, knot7, knot8, tail):
    knot1 = check(head, knot1, 'N')
    knot2 = check(knot1, knot2, 'N')
    knot3 = check(knot2, knot3, 'N')
    knot4 = check(knot3, knot4, 'N')
    knot5 = check(knot4, knot5, 'N')
    knot6 = check(knot5, knot6, 'N')
    knot7 = check(knot6, knot7, 'N')
    knot8 = check(knot7, knot8, 'N')
    tail = check(knot8, tail, 'Y')
    return (head, knot1, knot2, knot3, knot4, knot5, knot6, knot7, knot8, tail)

dh = {'L': -1, 'R': 1, 'U' : 0, 'D': 0}
dv = {'L': 0, 'R': 0, 'U' : 1, 'D': -1}

for move in info:
        for i in range(move[1]):
            head = (head[0] + dh[move[0]], head[1] + dv[move[0]])
            (head, knot1, knot2, knot3, knot4, knot5, knot6, knot7, knot8, tail) = run(head, knot1, knot2, knot3, knot4, knot5, knot6, knot7, knot8, tail)   

print(len(tailpositions))
