import heapq

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def is_wall(pos, design_number):
    x, y = pos
    value = x*x + 3*x + 2*x*y + y + y*y + design_number
    cnt_ones = 0
    while value:
        if value & 1:
            cnt_ones += 1
        value >>= 1
    return bool(cnt_ones & 1)

def manhatten(pos1, pos2):
    x1,y1 = pos1
    x2,y2 = pos2
    return abs(x1-x2) + abs(y1-y2)

def neighbors(pos):
    ox,oy = pos
    for dx, dy in dirs:
        x = ox + dx
        y = oy + dy
        if x >= 0 and y >= 0:
            yield (x,y)


def part1(inp):
    design_number = int(inp.strip())
    target = (31,39)

    pos = (1,1)
    dists = {pos: 0}
    queue = []
    heapq.heappush(queue, (0, pos))
    wall = set()

    while queue:
        priority, pos = heapq.heappop(queue)
        if pos == target:
            return dists[pos]

        for n_pos in neighbors(pos):
            if n_pos in wall:
                continue

            if is_wall(n_pos, design_number):
                wall.add(n_pos)
                continue

            dist = dists[pos] + 1
            if n_pos not in dists or dist < dists[n_pos]:
                dists[n_pos] = dist
                priority = dists[pos] + manhatten(n_pos, target)
                heapq.heappush(queue, (priority, n_pos) )


def part2(inp):
    design_number = int(inp.strip())

    pos = (1,1)
    dists = {pos: 0}
    queue = []
    heapq.heappush(queue, (0, pos))
    wall = set()

    while queue:
        priority, pos = heapq.heappop(queue)

        for n_pos in neighbors(pos):
            if n_pos in wall:
                continue

            if is_wall(n_pos, design_number):
                wall.add(n_pos)
                continue

            dist = dists[pos] + 1
            if dist > 50:
                continue

            if n_pos not in dists or dist < dists[n_pos]:
                dists[n_pos] = dist
                heapq.heappush(queue, (dist, n_pos) )
    return len(dists)


import unittest
class Test(unittest.TestCase):
    def test_is_wall(self):
        design_number = 10
        self.assertFalse(is_wall(0,0, design_number))
        self.assertTrue(is_wall(1,0, design_number))

        self.assertFalse(is_wall(4, 2, design_number))
        self.assertTrue(is_wall(8, 6, design_number))

    def test_manhatten(self):
        self.assertEqual(manhatten( (0,0), (10,20) ), 30)
        self.assertEqual(manhatten( (4,4), (2,1) ), 5)

    def test_neighbors(self):
        self.assertEqual(set(neighbors((0,0))),
                {(0,1), (1,0)})
        self.assertEqual(set(neighbors((5,3))),
                {(4,3), (6,3), (5,2), (5,4)})
