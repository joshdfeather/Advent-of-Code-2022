import re
import operator

lines = []
with open("input21.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

numbers = {}
expressions = {}
operations = ['+', '-', '*', '/']
ops = { "+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul}
for line in lines: 
    # Check if line is number and if so add to numbers
    if line[-1].isdigit():
        name, num = line.split(':')
        name, num = name, int(num.strip())
        numbers[name] = num
    # Otherwise format expression to store id1 : [id2, id3, op] in expressions 
    else: 
        id1, expr = line.split(':')
        x = operations[0]
        for arithmetic in operations:
            if arithmetic in expr:
                x = arithmetic
        ids = re.split(r'[/*+-]', str(expr))
        id2, id3 = ids[0].strip(), ids[1].strip()
        expressions[id1] = [id2, id3, x]


while True:
    for expr in expressions:
        if expressions[expr][0] in numbers and expressions[expr][1] in numbers:
            operator = expressions[expr][2]
            # Apply operation and store when both ids calculated
            numbers[expr] = ops[operator](numbers[expressions[expr][0]], numbers[expressions[expr][1]])
    # Break out of loop when numbers is full size
    if len(numbers) == len(lines):
        print(f"Part 1: {int(numbers['root'])}")
        break
