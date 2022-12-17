#!/usr/bin/env python

def sand():
    if sand_source in rock:
        return 0
    
    loc = sand_source
    while True:
        maybe = (loc[0] + 1, loc[1])
        if maybe not in rock:
            loc = maybe
            continue

        maybe = (loc[0] + 1, loc[1] - 1)
        if maybe not in rock:
            loc = maybe
            continue
        
        maybe = (loc[0] + 1, loc[1] + 1)
        if maybe not in rock:
            loc = maybe
            continue

        rock[loc] = 2
        if loc[0] > max_row:
            return 2
        else:
            return 1

rock_lines = []
with open("./day14_input.txt") as f:
    for record in f:
        rock_lines.append([list(map(int, p.strip().split(','))) for p in record.strip().split('->')])

rock = {}
max_row = 0
sand_source = (0, 500)

# build rock hash from input
for line in rock_lines:
    for idx in range(1, len(line)):
        start_r = int(line[idx-1][1])
        start_c = int(line[idx-1][0])
        trailing_r = int(line[idx][1])
        trailing_c = int(line[idx][0])
        if start_r > max_row:
            max_row = start_r
        if trailing_r > max_row:
            max_row = trailing_r
        if start_r == trailing_r:    
            if start_c > trailing_c:
                start_c, trailing_c = trailing_c, start_c
            for c in range(start_c, trailing_c+1):
                rock[(start_r, c)] = 1
        else:   # row varies
            if start_r > trailing_r:
                start_r, trailing_r = trailing_r, start_r
            for r in range(start_r, trailing_r+1):
                rock[(r, start_c)] = 1

for c in range(500 - max_row - 10, 500 + max_row + 10):
    rock[(max_row+2, c)] = 1

sitting_sand = 0
while sand() != 2:
    sitting_sand += 1

floor_sand = sitting_sand + 1 
while sand() != 0:
    floor_sand += 1 

print('Sand sitting including the floor: %d' % floor_sand)
