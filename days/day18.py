rules = set([
    (True, True, False),
    (False, True, True),
    (True, False, False),
    (False, False, True)
])

trap = '^'
safe = '.'

def count_safe(row):
    return sum(tile == safe for tile in row)

def gen_next_row(row):
    next_row = []
    hi = len(row) - 1

    for i, tile in enumerate(row):
        left = row[i-1] == trap if i > 0 else False
        center = row[i] == trap
        right = row[i+1] == trap if i < hi else False

        if (left, center, right) in rules:
            next_row.append(trap)
        else:
            next_row.append(safe)
    return next_row


def solve(row, n):
    cnt = count_safe(row)
    for _ in range(n-1):
        row = gen_next_row(row)
        cnt += count_safe(row)
    return cnt


def part1(inp):
    row = inp.strip()
    return solve(row, 40)

def part2(inp):
    row = inp.strip()
    return solve(row, 400_000)

