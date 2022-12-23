#! /usr/bin/env python
from enum import Enum
from dataclasses import dataclass


class Tile(Enum):
    OPEN = '.'
    SOLID = '#'
    NONE = ' '


class Direction(Enum):
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3


score: dict[Direction, int] = {Direction(i): i for i in range(4)}


def turn(direction: Direction, instruction: str):
    if instruction == 'L':
        return Direction((score[direction] - 1) % 4)
    elif instruction == 'R':
        return Direction((score[direction] + 1) % 4)


def opposite(direction: Direction):
    return turn(turn(direction, 'L'), 'L')


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)


def get_grid():
    grid = {}
    starting_position = None

    with open('day22_input.txt') as f:
        lines =  f.read().splitlines()
    
    for idx, line in enumerate(lines):
        if line == '':
            break
        for idx2, c in enumerate(line):
            pos = Position(idx2 + 1, idx + 1)
            grid[pos] = Tile(c)

            if starting_position is None and grid[pos] != Tile.NONE:
                starting_position = pos

    instructions_str = lines[-1]
    instructions = []
    current_number = 0
    for instruction in instructions_str:  # 10R5L5R10L4R5L5
        if instruction.isdigit():
            current_number = 10 * current_number + int(instruction)
        else:
            instructions.append(current_number)
            current_number = 0
            instructions.append(instruction)
    instructions.append(current_number)

    return grid, starting_position, instructions


def step(position: Position, direction: Direction):
    astep = {
        Direction.RIGHT: Position(1, 0),
        Direction.DOWN: Position(0, 1),
        Direction.LEFT: Position(-1, 0),
        Direction.UP: Position(0, -1),
    }

    return position + astep[direction]


def walk(grid, starting_position, instructions):
    current_direction: Direction = Direction.RIGHT
    current_position: Position = starting_position

    for instruction in instructions:
        if isinstance(instruction, str):
            current_direction = turn(current_direction, instruction)
        elif isinstance(instruction, int):
            current_position = walk_straight(grid,
                                             current_position,
                                             current_direction,
                                             nrof_steps=instruction)
    return current_position, current_direction


def walk_straight(grid, current_position, current_direction, nrof_steps: int):
    for _ in range(nrof_steps):
        new_position = step(current_position, current_direction)
        new_tile = grid.get(new_position, Tile.NONE)

        if new_tile == Tile.SOLID:
            return current_position

        if new_tile == Tile.OPEN:
            current_position = new_position

        if new_tile == Tile.NONE:
            '''
            . . . # . .
            . . . . . .
            X . # . . >
            . . . V . .
            '''
            opposite_direction = opposite(current_direction)
            fly_back_position = current_position
            while grid.get(fly_back_position, Tile.NONE) != Tile.NONE:
                fly_back_position = step(fly_back_position,
                                         opposite_direction)
            new_position = step(fly_back_position, current_direction)

            if grid[new_position] == Tile.SOLID:
                return current_position

            current_position = new_position

    return current_position


def walk_the_line():
    grid, starting_position, instructions = get_grid()
    final_position, final_direction = walk(
        grid,
        starting_position,
        instructions
    )
    
    return (
            1000 * final_position.y
            + 4 * final_position.x
            + score[final_direction]
    )



if __name__ == '__main__':
    passwd = walk_the_line()
    print('Password based on the path is: %d' % passwd)

