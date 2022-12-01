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

elf_with_the_most = 0

for elf in range(0, len(elf_calories)):
  if elf_calories[elf] > elf_with_the_most:
    elf_with_the_most = elf_calories[elf]

print("The elf has this many Calories: %s" % str(elf_with_the_most))
  
