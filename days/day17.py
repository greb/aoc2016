import hashlib
import heapq

grid_size = 4

def neighbors(passcode, pos, path):
    dirs = (
        ('U', (0, -1)),
        ('D', (0, 1)),
        ('L', (-1, 0)),
        ('R', (1, 0))
    )

    neighbors = []
    data = (passcode + path).encode()
    codes = hashlib.md5(data).hexdigest()

    for (dir, delta), code in zip(dirs, codes):
        x,y = (pos[0]+delta[0], pos[1]+delta[1])

        if code <= 'a':
            continue
        if not (0 <= x < grid_size):
            continue
        if not (0 <= y < grid_size):
            continue

        neighbors.append((dir, (x,y)))
    return neighbors


def find_shortest_path(passcode):
    pos = (0,0)
    target = (grid_size-1,grid_size-1)
    queue = [(0, pos, '')]

    while queue:
        _, pos, path = heapq.heappop(queue)
        if pos == target:
            break
        for dir, new_pos in neighbors(passcode, pos, path):
            new_path = path + dir
            prio = len(new_path)
            heapq.heappush(queue, (prio, new_pos, new_path))

    return path


def find_longest_path(passcode):
    pos = (0,0)
    target = (grid_size-1,grid_size-1)
    stack = [(pos, '')]
    len_path = 0

    while stack:
        pos, path = stack.pop()
        for dir, new_pos in neighbors(passcode, pos, path):
            new_path = path + dir

            if new_pos == target:
                if len(new_path) > len_path:
                    len_path = len(new_path)
            else:
                stack.append((new_pos, new_path))

    return len_path


def part1(inp):
    passcode = inp.strip()
    return find_shortest_path(passcode)


def part2(inp):
    passcode = inp.strip()
    return find_longest_path(passcode)


import unittest
class Test(unittest.TestCase):
    def test_find_shortest_path(self):
        self.assertEqual(
                find_shortest_path('kglvqrro'),
                'DDUDRLRRUDRD')
        self.assertEqual(
                find_shortest_path('ulqzkmiv'),
                'DRURDRUDDLLDLUURRDULRLDUUDDDRR')

    def test_find_longes_path(self):
        self.assertEqual( find_longest_path('kglvqrro'), 492)
        self.assertEqual( find_longest_path('ulqzkmiv'), 830)
