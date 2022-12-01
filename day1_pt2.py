#! /usr/bin/env python

elf_calories = []

with open("./day1_input.txt") as f:
  tmp_sum = 0
  for line in f.readlines():
    if line != "\n":
      tmp_sum += int(line)
    else:
      elf_calories.append(tmp_sum)
      tmp_sum =0

elves_with_the_most = [0,0,0]

for elf in range(0, len(elf_calories)):
  for pos in range(0,3):
    if elf_calories[elf] > elves_with_the_most[pos]:
      elves_with_the_most.insert(pos, elf_calories[elf])
      break
  elves_with_the_most = elves_with_the_most[:3]
    
print("The top 3 elves have this many Calories: %s" % str(sum(elves_with_the_most)))
  
