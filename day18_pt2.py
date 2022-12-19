#!/usr/bin/env python3
from itertools import product
from collections import deque

def neighbors(x, y, z):
    yield (x + 1, y    , z    )
    yield (x - 1, y    , z    )
    yield (x    , y + 1, z    )
    yield (x    , y - 1, z    )
    yield (x    , y    , z + 1)
    yield (x    , y    , z - 1)

def escape(cubes, src, rangex, rangey, rangez):
    seen = set()
    queue = deque([src])
    faces_touched = 0

    while queue:
        p = queue.pop()
        if p in seen:
            continue

        seen.add(p)
        x, y, z, = p

        if x not in rangex or y not in rangey or z not in rangez:
            return 0, seen

        for n in neighbors(x, y, z):
            if n in cubes:
                faces_touched += 1
            else:
                if n not in seen:
                    queue.append(n)

    return faces_touched, seen

cubes = {}

with open("./day18_input.txt") as f:
    for line in f:
        cubes[tuple(map(int, line.split(',')))] = 6

for cube in cubes:
    for n in neighbors(*cube):
        if n in cubes:
            cubes[cube] -= 1

minx = miny = minz = float('inf')
maxx = maxy = maxz = 0

for x, y, z in cubes:
    minx, maxx = min(x, minx), max(x, maxx)
    miny, maxy = min(y, miny), max(y, maxy)
    minz, maxz = min(z, minz), max(z, maxz)

rangex = range(minx, maxx + 1)
rangey = range(miny, maxy + 1)
rangez = range(minz, maxz + 1)


allseen = set()
surface = sum(cubes.values())

for c in product(rangex, rangey, rangez):
    if c not in cubes: 
        if c not in allseen: 
            touched, seen = escape(cubes, c, rangex, rangey, rangez)
            allseen |= seen

            if touched > 0:
                surface -= touched

print('The number of external surfaces: %d' %  surface)

