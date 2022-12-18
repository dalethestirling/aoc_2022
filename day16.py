#!/usr/bin/env python3

from math import inf as INFINITY
from functools import partial
from operator import itemgetter
from itertools import combinations, product
from collections import defaultdict


def floyd_warshall(g):
    distance = defaultdict(lambda: defaultdict(lambda: INFINITY))

    for a, bs in g.items():
        distance[a][a] = 0

        for b in bs:
            distance[a][b] = 1
            distance[b][b] = 0

    for a, b, c in product(g, g, g):
        bc, ba, ac = distance[b][c], distance[b][a], distance[a][c]

        if ba + ac < bc:
            distance[b][c] = ba + ac

    return distance

def score(rates, valves):
    s = 0
    for v, t in valves.items():
        s += rates[v] * t
    return s

def solutions(distance, rates, valves, time=30, cur='AA', chosen={}):
    for nxt in valves:
        new_time = time - distance[cur][nxt] - 1
        if new_time < 2:
            continue

        new_chosen = chosen | {nxt: new_time}
        yield from solutions(distance, rates, valves - {nxt}, new_time, nxt, new_chosen)

    yield chosen


graph = defaultdict(list)
rates = {}

with open("./day16_input.txt") as f:
    for record in f:
        rates[record.strip().split()[1]] = int(record.strip().split()[4].strip(';').split('=')[1])

        for dst in [ c.strip(',') for c in record.strip().split()[9:] ]:
            graph[record.strip().split()[1]].append(dst)

good     = frozenset(filter(rates.get, graph))
distance = floyd_warshall(graph)
score    = partial(score, rates)
best     = max(map(score, solutions(distance, rates, good)))

print('Max flow rathe that can be achieved: %d' % best)
