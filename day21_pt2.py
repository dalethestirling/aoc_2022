#! /usr/bin/env python

master_values = {}
master_expressions = {}
root_compare = []
all_things_equal = False
starting_num = 0

with open('day21_input.txt') as f:
#with open('test.txt') as f:
    for line in f:
        if line.split(':')[0].strip() == 'root': 
            root_compare.append(line.split(':')[1].strip().split()[0])
            root_compare.append(line.split(':')[1].strip().split()[2])
        elif line.split(':')[0].strip() == 'humn':
            continue
        else:
            try:
                master_values[line.split(':')[0].strip()] = int(line.split(':')[1])
            except ValueError:
                master_expressions[line.split(':')[0].strip()] = line.split(':')[1].strip()

#print('init values', values)
#print('init expr', expressions)
pre_compute = True
while pre_compute:
    master_delete = []
    for key, expression in master_expressions.items():
        num1, expr, num2 = expression.split()
        if 'humn' in [num1, num2]:
            print('pre_compute complete')
            pre_compute = False
            break
        if num1 in master_values.keys() and num2 in master_values.keys():
            master_values[key] = eval('%s %s %s' % (master_values[num1], expr, master_values[num2]))
            master_delete.append(key)
    for key in master_delete:
        del master_expressions[key]

greater_than = True
multiplier = 10000000000
while not all_things_equal:
    print(starting_num)
    expressions = master_expressions.copy()
    values = master_values.copy()
    values['humn'] = starting_num
    while expressions:
        to_delete = []
        for key, expression in expressions.items():
            num1, expr, num2 = expression.split()
            if num1 in values.keys() and num2 in values.keys():
                values[key] = eval('%s %s %s' % (values[num1], expr, values[num2]))
                to_delete.append(key)
        for key in to_delete:
            del expressions[key]
    print(root_compare[0], values[root_compare[0]])
    print(root_compare[1], values[root_compare[1]])
    if int(values[root_compare[0]]) ==  int(values[root_compare[1]]):
        all_things_equal = True
    else:
        if values[root_compare[0]] < values[root_compare[1]] and greater_than:
            starting_num = starting_num-multiplier
            multiplier = multiplier-int(multiplier/2)
        starting_num += multiplier

#print('end values', values)
#print('end expr', expressions)

#print('The Monkey named root yelled: %d' % int(values['root']))
print(starting_num)
