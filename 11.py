import time

class Monkey():
    def __init__(self, items, throw, operation, opval, modval, inspections):
        self.items = items
        self.throw = throw
        self.operation = operation
        self.opval = opval
        self.modval = modval
        self.inspections = inspections
    
    def op(self, x):
        if self.operation == '+':
            return (x + self.opval)
        elif self.opval == 50:
            return x * x
        else:
            original = x
            for _ in range(self.opval - 1):
                 x = x + original
            return x
    
    def test1(self, item):
            new = self.op(item)
            new = new // 3
            if new % self.modval == 0:
                return (0, new)
            else:
                return (1, new)

    def test2(self, item):
            new = self.op(item)
            new %= divisor
            if new % self.modval == 0:
                return (0, new)
            else:
                return (1, new)

monkey0 = Monkey([76, 88, 96, 97, 58, 61, 67], [2, 3], '*', 19, 3, 0)
monkey1 = Monkey([93, 71, 79, 83, 69, 70, 94, 98], [5, 6], '+', 8, 11, 0)
monkey2 = Monkey([50, 74, 67, 92, 61, 76], [3, 1], '*', 13, 19, 0)
monkey3 = Monkey([76, 92], [1, 6], '+', 6, 5, 0)
monkey4 = Monkey([74, 94, 55, 87, 62], [2, 0], '+', 5, 2, 0)
monkey5 = Monkey([59, 62, 53, 62], [4, 7], '*', 50, 7, 0)
monkey6 = Monkey([62], [5, 7], '+', 2, 17, 0)
monkey7 = Monkey([85, 54, 53], [4, 0], '+', 3, 13, 0)

monkeys = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]

for _ in range(20):
    for monkey in monkeys:
        while monkey.items != []:
            x = monkey.test1(monkey.items[0])
            monkey.inspections += 1
            monkeys[monkey.throw[x[0]]].items.append(x[1])
            monkey.items.pop(0)

vals = []
for monkey in monkeys:
    vals.append(monkey.inspections)
vals.sort()

print(f'Part1 : {vals[-1] * vals[-2]}')

monkey0 = Monkey([76, 88, 96, 97, 58, 61, 67], [2, 3], '*', 19, 3, 0)
monkey1 = Monkey([93, 71, 79, 83, 69, 70, 94, 98], [5, 6], '+', 8, 11, 0)
monkey2 = Monkey([50, 74, 67, 92, 61, 76], [3, 1], '*', 13, 19, 0)
monkey3 = Monkey([76, 92], [1, 6], '+', 6, 5, 0)
monkey4 = Monkey([74, 94, 55, 87, 62], [2, 0], '+', 5, 2, 0)
monkey5 = Monkey([59, 62, 53, 62], [4, 7], '*', 50, 7, 0)
monkey6 = Monkey([62], [5, 7], '+', 2, 17, 0)
monkey7 = Monkey([85, 54, 53], [4, 0], '+', 3, 13, 0)

monkeys = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]

divisor = 1
for m in monkeys:
    divisor *= m.modval 

for i in range(10000):
    for monkey in monkeys:
        while monkey.items != []:
            x = monkey.test2(monkey.items[0])
            monkey.inspections += 1
            monkeys[monkey.throw[x[0]]].items.append(x[1])
            monkey.items.pop(0)

vals = []
for monkey in monkeys:
    vals.append(monkey.inspections)
vals.sort()

print(f'Part2 : {vals[-1] * vals[-2]}')
