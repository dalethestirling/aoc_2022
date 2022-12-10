#! /usr/bin/env python

intervals = [20, 60, 100, 140, 180, 220]
addx_cost = 2

X = 1
cycles = 0
signal = []

with open("./day10_input.txt") as f:
    for instruct in f:
        if instruct.startswith('addx'):
            for i in range(addx_cost):
                cycles += 1
                if cycles in intervals:
                    print('triggered', cycles)
                    signal.append(cycles*X)
            X += int(instruct.strip().split()[1])
        else:
            cycles += 1
            if cycles in intervals:
                print('triggered', cycles)
                signal.append(cycles*X)
                    
print('The SUM signal strength intervals is: %d' % sum(signal))
