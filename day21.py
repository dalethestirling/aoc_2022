#! /usr/bin/env python

values = {}
expressions = {}

with open('day21_input.txt') as f:
    for line in f:
        try:
            values[line.split(':')[0].strip()] = int(line.split(':')[1])
        except ValueError:
            expressions[line.split(':')[0].strip()] = line.split(':')[1].strip()


while expressions:
    to_delete = []
    for key, expression in expressions.items():
        num1, expr, num2 = expression.split()
        if num1 in values.keys() and num2 in values.keys():
            values[key] = eval('%s %s %s' % (values[num1], expr, values[num2]))
            to_delete.append(key)
    for key in to_delete:
        del expressions[key]


print('The Monkey named root yelled: %d' % int(values['root']))
