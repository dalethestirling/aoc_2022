#! /usr/bin/env python

heightmap = []

def bfs(maze, start, end):
    queue = [(start, 0)]
    visited = set()
    best = 100000

    while len(queue) > 0:
        (curr, score) = queue.pop(0)
        if curr == end:
            if score < best:
                best = score
            continue

        if curr in visited:
            continue

        visited.add(curr)

        up = (curr[0], curr[1] - 1)
        down = (curr[0], curr[1] + 1)
        left = (curr[0] - 1, curr[1])
        right = (curr[0] + 1, curr[1])

        for dir in [up, down, left, right]:
            if dir[0] >= 0 and dir[0] < len(maze[0]) and dir[1] >= 0 and dir[1] < len(maze):
                current_height = maze[curr[1]][curr[0]]
                if current_height == "S":
                    current_height = "a"

                new_height = maze[dir[1]][dir[0]]

                if new_height == "E":
                    new_height = "z"

                if ord(current_height) + 1 >= ord(new_height):
                    queue.append((dir, score + 1))

    return best


with open("./day12_input.txt") as f:
    for line in f:
        heightmap.append(list(line.strip()))

start = (0, 0)
end = (0, 0)
a_positions = []

for (idx_row, row) in enumerate(heightmap):
    for (idx_cell, cell) in enumerate(row):
        if cell == "S":
            start = (idx_cell, idx_row)
        elif cell == "E":
            end = (idx_cell, idx_row)

print("Steps to get to the top: %d " % bfs(heightmap, start, end))
