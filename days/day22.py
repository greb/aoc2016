import re
import heapq

def parse(inp):
    nodes = {}
    for line in inp.splitlines()[2:]:
        words = line.split()
        pos = re.match(r'.*x(\d+)\-y(\d+)', words[0]).groups()
        pos = tuple(map(int, pos))
        used  = int(words[2][:-1])
        avail = int(words[3][:-1])
        nodes[pos] = used, avail
    return nodes

def part1(inp):
    nodes = parse(inp)

    cnt = 0
    for pos_a, (used, _) in nodes.items():
        for pos_b, (_, avail) in nodes.items():
            if used == 0:
                continue
            if pos_a == pos_b:
                continue
            if avail >= used:
                cnt += 1
    return cnt

def find_path(start, end, nodes, blocked=None):
    dist = dict()
    prev = dict()
    queue = [(0, start)]
    dist[start] = 0

    while queue:
        _, node = heapq.heappop(queue)
        neighbors = [(node[0]+1, node[1]), (node[0]-1, node[1]),
                     (node[0], node[1]+1), (node[0], node[1]-1)]
        if node == end:
            path = [node]
            while node in prev:
                path.append(prev[node])
                node = prev[node]
            return path

        for nxt in neighbors:
            if nxt not in nodes:
                continue
            if nodes[nxt][0] < 100 and nxt != blocked:
                new_dist = dist[node] + 1
                if nxt not in dist or dist[nxt] > new_dist:
                    dist[nxt] = new_dist
                    prev[nxt] = node
                    heapq.heappush(queue, (new_dist, nxt))

def print_grid(nodes, empty, goal, path):
    x_max = max(n[0] for n in nodes)
    y_max = max(n[1] for n in nodes)

    for y in range(y_max+1):
        row = []
        for x in range(x_max+1):
            if (x, y) == empty:
                row.append('_')
            elif (x, y) == goal:
                row.append('G')
            elif (x, y) in path:
                row.append('$')
            elif nodes[(x,y)][0] >= 100:
                row.append('#')
            else:
                row.append('.')
        print(''.join(row))
    print()


def part2(inp):
    nodes = parse(inp)
    x_max = max(n[0] for n in nodes)

    for node,val in nodes.items():
        if val[0] == 0:
            empty = node
            break

    start = (0,0)
    goal  = (x_max, 0)
    cnt = 0
    main_path = list(reversed(find_path(start, goal, nodes)))[:-1]

    while start != goal:
        new_goal = main_path.pop()
        path = find_path(empty, new_goal, nodes, blocked=goal)
        cnt += len(path)
        empty = goal
        goal = new_goal
    return cnt

