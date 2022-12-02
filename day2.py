#! /usr/bin/env python

def get_hand(val):
  # Rock
  if val in ['A', 'X']:
    return 1
  # Paper
  elif val in ['B', 'Y']:
    return 2
  # Scissors 
  elif val in ['C', 'Z']:
    return 3

victories = {
  1: [3],
  2: [1],
  3: [2]
  }

score = 0 

with open("./day2_input.txt") as f:
  for line in f:
    #print(line)
    a, b = [ get_hand(i) for i in line.split()]
    #print('%s, %s' % (a,b))
    if a == b:
      score += (3 + b)
    elif a in victories[b]:
      score += (6 + b)
    else:
      score += b
    #print(score)
    #break

print('Total score: %d' % score)
      
