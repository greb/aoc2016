import heapq
import itertools

from pprint import pprint

def parse(inp):
    numbers = dict()
    grid = list()
    for y, row in enumerate(inp.splitlines()):
        for x, tile in enumerate(row):
            if tile.isdigit():
                numbers[int(tile)] = (x,y)
        grid.append(row)
    return grid, numbers


def manhatten(pos0, pos1):
    return abs(pos0[0] - pos1[0]) + abs(pos0[1] - pos1[1])


def shortest_length(start, end, grid):
    dists = dict()
    visited = set()
    #prev = dict()

    dists[start] = 0
    queue = [(0, start)]

    while queue:
        _, node = heapq.heappop(queue)
        if node == end:
            break
        visited.add(node)

        neighbors = [(node[0]+1, node[1]), (node[0]-1, node[1]),
                    (node[0], node[1]+1), (node[0], node[1]-1)]

        for neigh in neighbors:
            x,y = neigh
            if grid[y][x] == '#':
                continue
            if neigh in visited:
                continue

            new_dist = dists[node] + 1
            if neigh not in dists or new_dist < dists[neigh]:
                dists[neigh] = new_dist
                #prev[neigh] = node
                prio = new_dist + manhatten(neigh, end)
                heapq.heappush(queue, (prio, neigh))
    
    #path = [end]
    #node = end
    #while node in prev:
    #    path.append(prev[node])
    #    node = prev[node]
    #print(start, end, len(path))

    return dists[end]

def shortest_number_dists(numbers, grid):
    number_dists = dict()
    for start, end in itertools.combinations(numbers.keys(), r=2):
        dist = shortest_length(numbers[start], numbers[end], grid)
        number_dists[(start, end)] = dist
        number_dists[(end, start)] = dist
    return number_dists

def part1(inp):
    grid, numbers = parse(inp)
    number_dists = shortest_number_dists(numbers, grid)

    path_lengths = []
    for path in itertools.permutations(numbers.keys()):
        path_length = 0
        for a,b in zip(path, path[1:]):
            path_length += number_dists[(a,b)]
        path_lengths.append(path_length)

    return min(path_lengths)


def part2(inp):
    grid, numbers = parse(inp)
    number_dists = shortest_number_dists(numbers, grid)

    nums = [n for n in numbers.keys() if n != 0]
    path_lengths = []
    for path in itertools.permutations(nums):
        path = [0] + list(path) + [0]
        path_length = 0
        for a,b in zip(path, path[1:]):
            path_length += number_dists[(a,b)]
        path_lengths.append(path_length)

    return min(path_lengths)
