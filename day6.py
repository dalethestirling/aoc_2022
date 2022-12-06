#! /usr/bin/env python

counter = 0

with open("./day6_input.txt") as f:
  for line in f:
    unique_flag = set()
    for letter in [*line]:
      counter+=1
      if letter not in unique_flag:
        unique_flag.add(letter)
        if len(unique_flag) == 4:
          break
      else:
        unique_flag = set()

print('Chars processed: %d' % counter)
