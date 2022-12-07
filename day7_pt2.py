#! /usr/bin/env python

from collections import defaultdict

dir = defaultdict(int)
root = []

with open("./day7_input.txt") as f:
  for cmd in f:
    match cmd.split():
        case ['$', 'cd', '..']:
            root.pop()
        case ['$', 'cd', p]:
            root.append(p)
        case ['$', 'ls']:
            pass
        case ['dir', p]:
            pass
        case [s, f]:
            dir[tuple(root)] += int(s)
            # add file size to each parent
            path = root[:-1]
            while path:
                dir[tuple(path)] += int(s)
                path.pop()

print(dir)
free = 70_000_000 - dir[('/',)]
print(min([d for d in dir.values() if d + free >= 30_000_000]))
