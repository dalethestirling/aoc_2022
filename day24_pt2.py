#! /usr/bin/env python
from dataclasses import dataclass

@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)


movement = {
    ">": Position(1, 0),
    "<": Position(-1, 0),
    "v": Position(0, 1),
    "^": Position(0, -1),
}

class Blizzard:
    width = None
    height = None

    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def move(self):
        self.position += self.direction

        x, y = self.position.x, self.position.y
        if x < 1:
            x = self.width-2
        if x > self.width-2:
            x = 1
        if y < 1:
            y = self.height-2
        if y > self.height-2:
            y = 1
        self.position = Position(x, y)


def get_blizzards():
    blizzards = []
    
    with open("day24_input.txt") as f:
        lines =  f.read().splitlines()
    
    height = len(lines)
    width = len(lines[0])

    Blizzard.width = width
    Blizzard.height = height

    valley = set()

    for j, line in enumerate(lines):
        for i, c in enumerate(line):
            if c == "#":
                continue

            pos = Position(i, j)
            valley.add(pos)

            if c == ".":
                continue

            blizzard = Blizzard(pos, direction=movement[c])
            blizzards.append(blizzard)

    return blizzards, valley, width, height


def navigate(possible_positions, blizzards, valley):
    for blizzard in blizzards:
        blizzard.move()

    blizzard_positions = {blizzard.position for blizzard in blizzards}
    clear_positions = valley - blizzard_positions

    reachable = {pos for pos in possible_positions}
    for position in possible_positions:
        for step in movement.values():
            reachable.add(position + step)

    new_possible_positions = reachable.intersection(clear_positions)
    return new_possible_positions


def reach_y_of(y, starting_position, blizzards, grid):
    possible_positions = {starting_position}
    idx = 0
    while True:
        idx += 1
        possible_positions = navigate(possible_positions, blizzards, grid)

        for pos in possible_positions:
            if pos.y == y:
                return idx, pos

if __name__ == "__main__":
    blizzards, valley, width, height = get_blizzards()

    there, pos = reach_y_of(height - 1, Position(1, 0), blizzards, valley)
    back, pos = reach_y_of(0, pos, blizzards, valley)
    again, _ = reach_y_of(height - 1, pos, blizzards, valley)

    print('The number of minuites it took to get there and back: %d' % (there + back + again))
