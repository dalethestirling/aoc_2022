#!/usr/bin/env python
import math

def manhattan_distance(record):
    return abs(record[0][0]-record[1][0])+abs(record[0][1]-record[1][1])

def find_consumed_for_row(data, row=2_000_000):
    min_x, max_x = math.inf, -math.inf
    
    for record in data:
        diev_y = abs(row - record[0][1])
        if diev_y > record[2]:
            continue
        diev_x = record[2] - diev_y
        min_x = min(record[0][0] - diev_x, min_x)
        max_x = max(record[0][0] + diev_x, max_x)
    return max_x - min_x

if __name__ == '__main__':
    sensor_data = []
    with open("./day15_input.txt") as f:
        for record in f:
            # Get (x,y), (x,y)
            split_record = record.strip().split()
            sensor_data.append([
                (
                    int(split_record[2].strip(',').split('=')[1]), 
                    int(split_record[3].strip(':').split('=')[1])
                ),
                (
                    int(split_record[8].strip(',').split('=')[1]),
                    int(split_record[9].strip().split('=')[1])
                )
            ])

for sensor in sensor_data:
    sensor.append(manhattan_distance(sensor))

print('Rows consumed in Y=2000000: %d' % find_consumed_for_row(sensor_data))
