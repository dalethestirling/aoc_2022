#! /usr/bin/env python

addx_cost = 2

PX=0
X = 1
cycles = 0
signal = []
CRT = ['.'] * 240

with open("./day10_input.txt") as f:
    for instruct in f:
        if instruct.startswith('addx'):
            for i in range(addx_cost):
                if cycles <= 240:
                    for row in range(0,240,40):
                        if cycles in range(row, row+39):
                            sprite = (row+(X-1), row+X, row+(X+1))
                            if cycles in sprite:
                                CRT[cycles] = '#'
                cycles += 1
            X += int(instruct.strip().split()[1])
        else:
            if cycles <= 240:
                for row in range(0,240,40):
                    if cycles in range(row, row+39):
                        sprite = (row+(X-1), row+X, row+(X+1))
                        if cycles in sprite:
                            CRT[cycles] = '#'
            cycles += 1

for start in range(0,240,40):
    print(''.join(CRT[start:start+39]))
