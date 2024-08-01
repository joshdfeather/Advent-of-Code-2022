
lines = []
counter = 0
minimum = 0

with open("input7.txt", "r") as file:
    for line in file:
        line = line[:-1]
        line = line.split(" ")
        lines.append(line)

class files():
    def __init__ (self, name, size, type):
        self.name = name
        self.size = size
        self.type = type

    def part1(self):
        return self.size

    def part2(self):
        return self.size
            
class directory():
    def __init__ (self, name, size, contents, type):
        self.name = name
        self.size = size
        self.contents = contents
        self.type = type

    def new(self, x):
        self.contents.append(x)

    def sizes(self):
        for i in self.contents:
            if i.type == "file":
                self.size += i.size
            elif i.type == "directory" and i.size != 0:
                self.size += i.size
            elif i.type == "directory" and i.size == 0:
                self.size += i.sizes()
        return self.size

    def part1(self):
        global counter
        for i in self.contents:
            if i.size <= 100000 and i.type == "directory":
                counter += i.size
            i.part1()
        return counter

    def part2(self):
        global minimum
        for i in self.contents:
            if i.size >= 10216456 and i.size < 50216456 and i.type == "directory":
                minimum = i.size
            i.part2()
        return minimum

outer = directory("outer", 0, [], "directory")
stack = []
stack.append(outer)

i = 1
while i < len(lines):
    if lines[i][1] == 'ls':
        i += 1
        while lines[i][0] != '$':
            if lines[i][0] == 'dir':
                d = directory(lines[i][-1], 0, [], "directory")
                stack[-1].new(d)
            else:
                f = files(lines[i][-1], int(lines[i][0], base = 10), "file")
                stack[-1].new(f)
            i += 1

            if i == 1001:
                break
        i -= 1
    elif lines[i][1] == 'cd':
        if lines[i][2] == '..':
            stack.pop()
        else: 
            for j in range(len(stack[-1].contents)):
                if stack[-1].contents[j].name == lines[i][2]:
                    stack.append(stack[-1].contents[j])
                    break
    i += 1

print("\n")
outer.sizes()
print(f'Part 1: {outer.part1()}')
print(f'Part 2: {outer.part2()}')
