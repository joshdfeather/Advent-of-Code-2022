
lines = []
tuples = []
characters = []

with open("input3.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

i = 0
while (i < len(lines)):
    tuples.append((lines[i], lines[i + 1], lines[i + 2]))
    i += 3

for tuple in tuples:
    for character in tuple[0]:
        if character in tuple[1] and character in tuple[2]:
            characters.append(character)
            break

max = 0

for character in characters:
    if character.lower() == character:
        max += ord(character) - 96
    else:
        max += ord(character) - 64 + 26

print(characters)
print(max)