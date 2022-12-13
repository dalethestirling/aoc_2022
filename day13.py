#! /usr/bin/env python

def ordered(left, right):
    if isinstance(left, int) & isinstance(right, int):
        if left < right: return 1
        elif right < left: return -1
        else: return 0
    elif isinstance(left, list) & isinstance(right, list):
        for i in range(min(len(left), len(right))):
            if ordered(left[i], right[i]) != 0:
                return ordered(left[i], right[i])
        if len(left) < len(right):
            return 1
        elif len(right) < len(left):
            return -1
        else:
            return 0
    elif isinstance(left, list) & isinstance(right, int):
        return ordered(left, [right])
    elif isinstance(left, int) & isinstance(right, list):
        return ordered([left], right)

pairs = []

with open("./day13_input.txt") as f:
    p = []
    for line in f:
        if line != '\n':
            p.append(eval(line.strip()))
        else:
            pairs.append(p)
            p = []
            
data = []
for idx, pair in enumerate(pairs):
    if ordered(*pair) == 1:
        data.append(idx+1)

print('Value of the destress instances: %d' %sum(data))
