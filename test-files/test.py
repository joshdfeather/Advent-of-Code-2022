# Day Ten

# Part One

text = open("input10.txt").read()

instructions = text.splitlines()

X_values = dict()
X = 1
cycle = 0

for inst in instructions:
    if inst.startswith("noop"):
        cycle += 1
        X_values[cycle] = X
    else:
        cycle += 1
        X_values[cycle] = X
        cycle += 1
        X_values[cycle] = X
        X += int(inst.split()[1])

print(sum(X_values[k] * k for k in range(20, 221, 40)))
    
# Part Two

print(X_values)

from textwrap import wrap

s = "".join("#" if X_values[cycle] - 1 <= (cycle % 40 - 1) % 40 <= X_values[cycle] + 1 else " " for cycle in range(1, 241))

print("\n".join(wrap(s, 40)))