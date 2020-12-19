import re

rotate = {
    'R': {'N':'E', 'E':'S', 'S':'W', 'W':'N'},
    'L': {'N':'W', 'W':'S', 'S':'E', 'E':'N'}
}

delta = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0)
}

def parse(inp):
    path = re.findall(r'(.)(\d+)', inp)
    return [(r, int(d)) for r, d in path]

def distance(x,y):
    return abs(x) + abs(y)

def part1(inp):
    path = parse(inp)

    dir_ = 'N'
    x, y = 0,0

    for rot, dist in path:
        dir_ = rotate[rot][dir_]
        dx, dy = delta[dir_]

        x += dist * dx
        y += dist * dy

    return distance(x,y)


def part2(inp):
    path = parse(inp)
    visited = set()

    dir_ = 'N'
    x, y = 0,0

    for rot, dist in path:
        dir_ = rotate[rot][dir_]
        dx, dy = delta[dir_]

        for _ in range(dist):
            x += dx
            y += dy

            if (x,y) in visited:
                return distance(x,y)
            visited.add((x,y))
