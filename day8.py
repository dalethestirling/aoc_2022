#! /usr/bin/env python

forest = []

def check_vertical(row, column, forest=forest):
    # Consider tree visible by default
    up = True
    down = True

    tree = forest[row][column]
    neighbours_up = list(reversed(range(0, row)))
    neighbours_down = list(range(row+1, len(forest)))
    for neighbour in neighbours_up:
        if tree <= forest[neighbour][column]:
            up = False
            break
    for neighbour in neighbours_down:
        if tree <= forest[neighbour][column]:
            down = False
            break

    return [up, down]
        
def check_horizontal(row, column, forest=forest):
    # Consider tree visible by default
    left = True
    right = True

    tree = forest[row][column]
    neighbours_left = list(reversed(range(0, column)))
    neighbours_right = list(range(column+1, len(forest[row])))
    for neighbour in neighbours_left:
        if tree <= forest[row][neighbour]:
            left = False
            break
    for neighbour in neighbours_right:
        if tree <= forest[row][neighbour]:
            right = False
            break

    return [left, right]

# build forest grid
with open("./day8_input.txt") as f:
    for line in f:
        forest.append([*line.strip()])

vertical_edge = [0, len(forest)-1]

visible_trees = ((len(forest)-2)*2)+(len(forest[0])*2)

for row in range(len(forest)):
    horizontal_edge = [0, len(forest[row])-1]
    if row not in vertical_edge:
        for tree in range(len(forest[row])):
            if tree not in horizontal_edge:
                vertical_result = check_vertical(row, tree)
                horizontal_result = check_horizontal(row, tree)
                if any(vertical_result+horizontal_result):
                   visible_trees += 1

print('The number of visible trees are: %d' % visible_trees)
