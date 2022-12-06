#! /usr/bin/env python

chunk = 14
counter = 0

with open("./day6_input.txt") as f:
  for line in f:
    for idx in range(14, len(line)-1):
      if len(set(line[idx-chunk:idx])) == chunk:
        print('Chars processed: %d' % idx)
        break


