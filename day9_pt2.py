#! /usr/bin/env python

num_of_ropes = 10
journey = set()

rope_knots = [[0, 0] for i in range(num_of_ropes)]
journey.add(tuple(rope_knots[-1]))

def move_tail(head, tail, movement):
    
    prev_tail = (tail[0], tail[1])

    if abs(tail[0] - head[0]) > 1 or abs(tail[1] - head[1]) > 1:
        if 0 not in movement:
            if tail[0] == head[0]:
                tail[1] += movement[1]
            elif tail[1] == head[1]:
                tail[0] += movement[0]
            else:
                tail[0] += movement[0]
                tail[1] += movement[1]
        else:
            tail[0] += movement[0]
            tail[1] += movement[1]

            if movement[0] != 0 and tail[1] != head[1]:
                tail[1] = head[1]
            elif movement[1] != 0 and tail[0] != head[0]:
                tail[0] = head[0]
    
    return (tail[0] - prev_tail[0], tail[1] - prev_tail[1])

move_head = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }

with open("./day9_input.txt") as f:
    for line in f:
        direction, steps = line.strip().split()
        for step in range(int(steps)):
            movement = move_head[direction]
            rope_knots[0][0] += movement[0]
            rope_knots[0][1] += movement[1]
            for rope in range(1, num_of_ropes):
                movement = move_tail(rope_knots[rope-1], rope_knots[rope], movement)
                if movement == (0, 0):
                    break
            journey.add(tuple(rope_knots[-1])) 

print('The tail took the folling number of movements: %d' % len(journey))
