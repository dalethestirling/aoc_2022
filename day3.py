#! /usr/bin/env python

valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority = { valid_chars[i]:i+1 for i in range(0, len(valid_chars))} 

score = 0 

with open("./day3_input.txt") as f:
  for line in f:
    line_count = 0
    compartment1 = line[int(len(line)/2):]
    compartment2 = line[:int(len(line)/2)]

    matched_items = list(set(compartment1).intersection(compartment2))

    for item in matched_items:
      if item in priority.keys():
        score += priority[item]

print('The match item score is: %s' % score)
