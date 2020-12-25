def parse(inp):
    ranges = []
    for line in inp.splitlines():
        r = [int(v) for v in line.split('-')]
        ranges.append(r)
    return ranges

def test_number(n, blocked):
    for lo, hi in blocked:
        if lo <= n <= hi:
            return False

    return n < 2**32

def part1(inp):
    blocked = parse(inp)
    blocked = sorted(blocked)
    canidates = [b[1]+1 for b in blocked]

    for canidate in canidates:
        if test_number(canidate, blocked):
            break
    return canidate

def part2(inp):
    blocked = parse(inp)
    blocked = sorted(blocked)
    canidates = [b[1]+1 for b in blocked]

    cnt = 0
    for canidate in canidates:
        while test_number(canidate, blocked):
            cnt += 1
            canidate += 1
    return cnt

