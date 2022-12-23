#! /usr/bin/env python

from enum import Enum
from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)


class Direction(Enum):
    N = 'north'
    NE = 'northeast'
    E = 'east'
    SE = 'southeast'
    S = 'south'
    SW = 'southwest'
    W = 'west'
    NW = 'northwest'


model = {
    Direction.N: Position(0, 1),
    Direction.NE: Position(1, 1),
    Direction.E: Position(1, 0),
    Direction.SE: Position(1, -1),
    Direction.S: Position(0, -1),
    Direction.SW: Position(-1, -1),
    Direction.W: Position(-1, 0),
    Direction.NW: Position(-1, 1),
}


neighbours = {
    Direction.N: [Direction.NW, Direction.NE],
    Direction.E: [Direction.NE, Direction.SE],
    Direction.S: [Direction.SE, Direction.SW],
    Direction.W: [Direction.SW, Direction.NW],
}

direction_map = [Direction.N, Direction.S, Direction.W, Direction.E]


def get_elf_positions():
    lines = []
    with open('day23_input.txt') as f:
        lines =  f.read().splitlines()
    
    elf_positions: list[Position] = []
    for j, line in enumerate(reversed(lines)):
        for i, c in enumerate(line):
            if c == '#':
                elf_positions.append(Position(i, j))

    print(f'Found {len(elf_positions)} elves.')
    return elf_positions


def do_round(elf_positions: list[Position], first_considered=0):
    proposed_positions: list[Position] = []
    proposed_so_far: set[Position] = set()
    duplicates: set[Position] = set()

    elf_set = set(elf_positions)

    for elf_position in elf_positions:

        if no_neighbours(elf_position, elf_set):
            proposed_positions.append(elf_position)
            continue

        for check_nr in range(4):
            check_id = (first_considered + check_nr) % 4
            check_direction = direction_map[check_id]

            if is_valid(check_direction, elf_position, elf_set):
                proposed_position = elf_position + model[check_direction]
                proposed_positions.append(proposed_position)
                if proposed_position in proposed_so_far:
                    duplicates.add(proposed_position)
                proposed_so_far.add(proposed_position)
                break
        else:  # No direction valid
            proposed_positions.append(elf_position)

    new_elf_positions = []
    for elf_position, proposed_position in zip(elf_positions,
                                               proposed_positions):
        if proposed_position in duplicates:
            new_elf_positions.append(elf_position)
        else:
            new_elf_positions.append(proposed_position)

    return new_elf_positions


def no_neighbours(elf_position, elf_positions):
    for direction in Direction:
        check_position = elf_position + model[direction]
        if check_position in elf_positions:
            return False
    return True


def is_valid(check_direction: Direction, position: Position, elf_positions):
    for direction in [check_direction] + neighbours[check_direction]:
        proposed_position = position + model[direction]
        if proposed_position in elf_positions:
            return False
    return True


def print_elf_positions(elf_positions):
    min_x = min(elf_position.x for elf_position in elf_positions)
    max_x = max(elf_position.x for elf_position in elf_positions)
    min_y = min(elf_position.y for elf_position in elf_positions)
    max_y = max(elf_position.y for elf_position in elf_positions)

    for y in range(max_y, min_y -1, -1):
        for x in range(min_x, max_x+1):
            if Position(x, y) in elf_positions:
                print('#', end='')
            else:
                print('.', end='')
        print()


def dance_elf_dance():
    elf_positions = get_elf_positions()

    for i in range(10):
        elf_positions = do_round(elf_positions, first_considered=i % 4)

    min_x = min(elf_position.x for elf_position in elf_positions)
    min_y = min(elf_position.y for elf_position in elf_positions)
    max_x = max(elf_position.x for elf_position in elf_positions)
    max_y = max(elf_position.y for elf_position in elf_positions)

    area = (max_x - min_x + 1) * (max_y - min_y + 1)
    return area - len(elf_positions)


if __name__ == '__main__':
    print('Number of availible space in the rectange of elves: %d' % dance_elf_dance())

