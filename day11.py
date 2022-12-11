#! /usr/bin/env python
from functools import reduce

class Monkey:
    def __init__(self):
        self.items =  []
        self.operation =  lambda old: eval(self.op_str)
        self.op_str = 'old'
        self.test =  None
        self.throw_true =  None
        self.throw_false = None

        self.inspected = 0

# Data model Vars
monkeys = {}
in_monkey = False
monkey_id = 0 

# Processing vars
num_rounds = 20
calm_down = 3
monkey_tracked = 2
rounds = 0

with open("./day11_input.txt") as f:
    for line in f:
        if line.startswith('Monkey'):
            monkey_id = int(line.strip().split()[1].strip(':'))
            monkeys[monkey_id] = Monkey()
            in_monkey = True
        elif line.strip().startswith('Starting') and in_monkey:
            monkeys[monkey_id].items = [int(item) for item in line.strip().split(':')[1].strip().split(',')]
        elif line.strip().startswith('Operation') and in_monkey:
            monkeys[monkey_id].op_str = line.strip().split(':')[1].split('=')[1].strip()
        elif line.strip().startswith('Test') and in_monkey:
            monkeys[monkey_id].test = int(line.strip().split('by')[1])
        elif line.strip().startswith('If true') and in_monkey:
            monkeys[monkey_id].throw_true = int(line.strip().split('monkey')[1])
        elif line.strip().startswith('If false') and in_monkey:
            monkeys[monkey_id].throw_false = int(line.strip().split('monkey')[1])
            in_monkey = False

while rounds < num_rounds:
    for monkey in monkeys:
        for _ in range(len(monkeys[monkey].items)):
            item = monkeys[monkey].items.pop()
            worry_adjusted = int(monkeys[monkey].operation(item)/calm_down)
            if worry_adjusted%monkeys[monkey].test == 0: 
                monkeys[monkeys[monkey].throw_true].items.append(worry_adjusted)
            else:
                monkeys[monkeys[monkey].throw_false].items.append(worry_adjusted)
            monkeys[monkey].inspected += 1
    rounds += 1 
    
print('Total monkey business: %d' % reduce((lambda x, y: x * y), sorted([ monkeys[i].inspected for i in monkeys ])[0-monkey_tracked:]))
