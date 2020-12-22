import re
import heapq
import itertools

from pprint import pprint

def parse(inp):
    floors = []
    for line in inp.splitlines():
        floor = set()
        chips = re.findall(r'(\S+)\-compatible microchip', line)
        floor.update(('M', c) for c in chips)
        gens = re.findall(r'(\S+) generator', line)
        floor.update(('G', g) for g in gens)
        floors.append(frozenset(floor))
    return (0, tuple(floors))


def is_safe(load):
    if len(load) <= 1:
        return True
    gens = [mat for kind, mat in load if kind == 'G']
    chips = [mat for kind, mat in load if kind == 'M']
    if not gens:
        return True

    for mat in chips:
        if mat not in gens:
            return False
    return True


def valid_moves(layout):
    num, floors = layout
    for direction in [-1, 1]:
        new_num = num + direction
        if not 0 <= new_num < 4:
            continue

        elevator_loads = itertools.chain(
            itertools.combinations(floors[num], 2),
            itertools.combinations(floors[num], 1))

        for load in elevator_loads:
            if not is_safe(load):
                continue

            new_floor = frozenset(floors[new_num] | set(load))
            if not is_safe(new_floor):
                continue

            old_floor = frozenset(floors[num] - set(load))
            if not is_safe(old_floor):
                continue

            new_floors = list(floors)
            new_floors[new_num] = new_floor
            new_floors[num] = old_floor
            yield new_num, tuple(new_floors)


def score_layout(layout):
    # The lower the score, the better. Zero means we hit the target
    score = 0
    for i, floor in enumerate(layout[1]):
        score += (3-i)*len(floor)
    return score

def search(layout):
    queue = []
    score = score_layout(layout)
    heapq.heappush(queue, (0, score, layout))
    dist = 0
    dists = {layout: dist}

    while queue:
        sum_score, score, current = heapq.heappop(queue)
        if score == 0:
            break

        for move in valid_moves(current):
            new_dist = dists[current] + 1
            if move not in dists or new_dist < dists[move]:
                dists[move] = new_dist
                new_score = score_layout(move)
                priority = new_dist+new_score
                heapq.heappush(queue, (priority, new_score, move) )

    return dists[current]


def part1(inp):
    layout = parse(inp)
    return search(layout)

def part2(inp):
    layout = parse(inp)

    floors = list(layout[1])
    floors[0] |= frozenset([('G', 'elerium'), ('M', 'elerium'),
        ('G', 'dilithium'), ('M', 'dilithium')])
    layout = layout[0], tuple(floors)

    return search(layout)
