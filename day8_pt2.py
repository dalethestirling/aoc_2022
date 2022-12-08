#! /usr/bin/env python

forest = []

def check_vertical(row, column, forest=forest):
    up = 0
    down = 0

    tree = forest[row][column]
    neighbours_up = list(reversed(range(0, row)))
    neighbours_down = list(range(row+1, len(forest)))
    for neighbour in neighbours_up:
        up += 1
        if tree <= forest[neighbour][column]:
            break
    for neighbour in neighbours_down:
        down += 1
        if tree <= forest[neighbour][column]:
            break

    return [up, down]
        
def check_horizontal(row, column, forest=forest):
    left = 0
    right = 0

    tree = forest[row][column]
    neighbours_left = list(reversed(range(0, column)))
    neighbours_right = list(range(column+1, len(forest[row])))
    for neighbour in neighbours_left:
        left += 1
        if tree <= forest[row][neighbour]:
            break
    for neighbour in neighbours_right:
        right += 1
        if tree <= forest[row][neighbour]:
            break

    return [left, right]

# build forest grid
with open("./day8_input.txt") as f:
    for line in f:
        forest.append([*line.strip()])

vertical_edge = [0, len(forest)-1]

best_view = 0

for row in range(len(forest)):
    horizontal_edge = [0, len(forest[row])-1]
    if row not in vertical_edge:
        for tree in range(len(forest[row])):
            if tree not in horizontal_edge:
                vertical_result = check_vertical(row, tree)
                horizontal_result = check_horizontal(row, tree)
                scenic_score = vertical_result[0]*horizontal_result[0]*horizontal_result[1]*vertical_result[1]
                if scenic_score > best_view:
                    best_view = scenic_score

print('The best scenic score for the forest is: %d' % best_view)
