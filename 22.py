import itertools
import math
import typing

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
NUM_DIRECTIONS = 4


def parse(path):
    with open(path) as f:
        # Split by double new line to seperate the grid from instructions
        txt = f.read().split("\n\n")
        instructions = txt[1].strip()
        grid = txt[0].splitlines()
        # Find longest line in grid
        max_length = max(len(l) for l in grid)
        # Fill grid with ' ' characters where needed
        grid = [l + " " * (max_length - len(l)) for l in grid]
        # Group insturctions into non digit characters and digits
        instructions = ["".join(v[1]) for v in itertools.groupby(instructions, key=lambda c: c.isdigit())]
        instructions = [int(v) if v[0].isdigit() else v for v in instructions]
    return instructions, grid


def part1(instructions, grid):
    num_rows = len(grid)
    num_col = len(grid[0])
    coord = [0, grid[0].index(".")]
    dindex = 0
    direction = DIRECTIONS[dindex]
    for instr in instructions:
        if instr == "R":
            dindex = (dindex + 1) % NUM_DIRECTIONS
            direction = DIRECTIONS[dindex]
        elif instr == "L":
            dindex = (dindex - 1) % NUM_DIRECTIONS
            direction = DIRECTIONS[dindex]
        else:
            for _ in range(instr):
                next_coord = list(coord)
                next_coord[0] = (next_coord[0] + direction[0]) % num_rows
                next_coord[1] = (next_coord[1] + direction[1]) % num_col

                if grid[next_coord[0]][next_coord[1]] == ".":
                    coord = next_coord
                elif grid[next_coord[0]][next_coord[1]] == "#":
                    break
                else:
                    while grid[next_coord[0]][next_coord[1]] == " ":
                        next_coord[0] = (next_coord[0] + direction[0]) % num_rows
                        next_coord[1] = (next_coord[1] + direction[1]) % num_col
                    if grid[next_coord[0]][next_coord[1]] == ".":
                        coord = next_coord
                    elif grid[next_coord[0]][next_coord[1]] == "#":
                        break
    return (coord[0] + 1) * 1000 + 4 * (coord[1] + 1) + dindex




def main():
    test_instructions, test_grid = parse("input22test.txt")
    instructions, grid = parse("input22.txt")

    assert part1(test_instructions, test_grid) == 6032
    print(part1(instructions, grid))



if __name__ == "__main__":
    main()