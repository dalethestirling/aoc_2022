#! /usr/bin/env python

duplicate_work = 0 

def get_nums(assignments):
  return list(range(int(assignments.split('-')[0]), int(assignments.split('-')[1])+1))

def test_contains(zones_a, zones_b):
  return any(item in zones_a for item in zones_b)

with open("./day4_input.txt") as f:
  for line in f:
    is_duplicate = False

    elf_a, elf_b = line.split(',')
    elf_a_zones = get_nums(elf_a)
    elf_b_zones = get_nums(elf_b)

    if test_contains(elf_a_zones, elf_b_zones):
      duplicate_work += 1
    elif test_contains(elf_b_zones, elf_a_zones):
      duplicate_work += 1

print('Pairs with duplicates: %d' % duplicate_work)
