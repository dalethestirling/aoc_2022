#!/usr/bin/env python

def swap(records, idx):
    i = records.index(idx)
    val, _ = records.pop(i)
    iNew = (i+val)%len(records)
    records.insert(iNew, idx)

def mix(entries, times = 1):
    new_list = [(n, i) for i, n in enumerate(entries)]
    for _ in range(times):
        for i, n in enumerate(entries):
            swap(new_list, (n, i))
    return [code[0] for code in new_list]

with open('day20_input.txt') as f:
    entries = [ line.strip() for line in f ]

l = [int(x) for x in entries]

dKey = 811589153
l = list(map(lambda x:x*dKey, l))
mixed = mix(l, 10)
s = sum(mixed[(i+mixed.index(0))%len(mixed)] for i in (1000, 2000, 3000))
print(s)
