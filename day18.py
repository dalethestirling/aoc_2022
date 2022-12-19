#!/usr/bin/env python3

def neighbors(x, y, z):
    yield (x + 1, y    , z    )
    yield (x - 1, y    , z    )
    yield (x    , y + 1, z    )
    yield (x    , y - 1, z    )
    yield (x    , y    , z + 1)
    yield (x    , y    , z - 1)

cubes = {}

with open("./day18_input.txt") as f:
    for line in f:
        cubes[tuple(map(int, line.split(',')))] = 6

for cube in cubes:
    for n in neighbors(*cube):
        if n in cubes:
            cubes[cube] -= 1

print('The number of exposed surfaces is: %d' % sum(cubes.values()))
