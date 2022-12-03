#! /usr/bin/env python

valid_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority = { valid_chars[i]:i+1 for i in range(0, len(valid_chars))} 

score = 0 
rucks = []

with open("./day3_input.txt") as f:
  for line in f:
    rucks.append(line.strip())
    
  for third in range(2, len(rucks), 3):
      
      ruck1 = { x for x in rucks[third-2]}
      ruck2 = { x for x in rucks[third-1]}
      ruck3 = { x for x in rucks[third]}

      matched_items = ruck1.intersection(ruck2, ruck3)
      for item in matched_items:
        if item in priority.keys():
          score += priority[item]
      
      line_list = []

print('The badge score is: %s' % score)
