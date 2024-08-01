
lines = []
tuples = []
characters = []

with open("input3.txt", "r") as file:
    for line in file:
        lines.append(line.strip())

for line in lines:
    string1 = line[0: int(len(line)/2)]
    string2 = line[int(len(line)/2): len(line)]
    tuples.append((string1, string2))

for tuple in tuples:
    for character in tuple[0]:
        if character in tuple[1]:
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