#! /usr/bin/env python
import re 

crates = {
 1: ['F', 'L', 'M', 'W'],
 2: ['F', 'M', 'V', 'Z', 'B'],
 3: ['Q', 'L', 'S', 'R', 'V', 'H'],
 4: ['J', 'T', 'M', 'P', 'Q', 'V', 'S', 'F'],
 5: ['W', 'S', 'L'],
 6: ['W', 'J', 'R', 'M', 'P', 'V', 'F'],
 7: ['F', 'R', 'N', 'P', 'C', 'Q', 'J'],
 8: ['B', 'R', 'W', 'Z', 'S', 'P', 'H', 'V'],
 9: ['W', 'Z', 'H', 'G', 'C', 'J', 'M', 'B']
 }

with open("./day5_input.txt") as f:
  for line in f:
    if re.match('move', line):
      line_list = line.split()
      dest = int(line_list[5])
      src = int(line_list[3])
      qty = int(line_list[1])
      # Move
      crates[dest] = crates[src][:qty] + list(crates[dest])
      # Remove
      crates[src] =  crates[src][qty:]

top_crates = []
for key in crates.keys():
  top_crates.append(crates[key][0])
print(''.join(top_crates))
