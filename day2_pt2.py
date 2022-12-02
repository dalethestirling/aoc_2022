#! /usr/bin/env python

def get_hand(val):
  # Rock
  if val in ['A']:
    return 1
  # Paper
  elif val in ['B']:
    return 2
  # Scissors 
  elif val in ['C']:
    return 3

def get_value(line):
  value, outcome = line.split()
  return '%s %s' % (value, how_to_act[value][outcome])

how_to_act = {
  'A': {
    'X': 'C',
    'Y': 'A',
    'Z': 'B'
  },
  'B': {
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
  },
  'C': {
    'X': 'B',
    'Y': 'C',
    'Z': 'A'
  }
}

victories = {
  1: [3],
  2: [1],
  3: [2]
  }

score = 0 

with open("./day2_input.txt") as f:
  for line in f:
    #print(line)
    a, b = [ get_hand(i) for i in get_value(line).split()]
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
      
