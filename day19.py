#! /usr/bin/env python
import re

with open('day19_input.txt', 'r') as f:
    blueprints = [ blueprint.strip() for blueprint in f.readlines() ] 

    blueprint_model = list()
    for blueprint in blueprints:
        ints = [int(datapoint) for datapoint in re.findall(r'\d+', blueprint)]
        blueprint_model.append(ints)

def optimise(state): 
    minutes, (robots, inventory, mined) = state
    return 1000 * mined[3] + 100 * mined[2] + 10 * mined[1] + mined[0]

def bfs(costs, robots, num_minutes, top_queue = 30000):
    queue = list()
    queue.append((0, (robots, (0, 0, 0, 0), (0, 0, 0, 0))))
    geodes_mined = 0
    depth = 0

    while queue: 
        minutes, (robots, old_inventory, mined) = queue.pop(0)

        if minutes > depth:
            queue.sort(key = optimise, reverse = True)
            queue = queue[:top_queue]
            depth = minutes

        if minutes == num_minutes:
            geodes_mined = max(geodes_mined, mined[3])
            continue 

        new_inventory = tuple([old_inventory[ii] + robots[ii] for ii in range(4)])
        new_mined = tuple([mined[ii] + robots[ii] for ii in range(4)])

        queue.append((minutes + 1, (robots, new_inventory, new_mined)))

        for r_id in range(4): 
            cost_robot = costs[r_id]

            if all([old_inventory[i_id] >= cost_robot[i_id] for i_id in range(4)]):
                new_robots = list(robots)
                new_robots[r_id] += 1
                new_robots = tuple(new_robots)

                new_inventory_state = tuple([new_inventory[i_id] - cost_robot[i_id] for i_id in range(4)])
                queue.append((minutes + 1, (new_robots, new_inventory_state, new_mined)))

    return geodes_mined

minutes = 24 
total_quality = 0
for bpid, cost_ore_robot, cost_clay_robot, ob_ore, obs_clay, geode_ore, geode_ob in blueprint_model:
    cost_per_robot = [
        (cost_ore_robot, 0, 0, 0),
        (cost_clay_robot, 0, 0, 0),
        (ob_ore, obs_clay, 0, 0),
        (geode_ore, 0, geode_ob, 0)
    ]
    mined = bfs(cost_per_robot, (1, 0, 0, 0), minutes, top_queue = 1000)

    total_quality += mined * bpid

print("Quality level for blueprint are: %d" % total_quality)
