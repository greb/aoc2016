def move_finger(m, x, y):
    if m == 'R' and x < 2:
        return (x+1, y)
    elif m == 'D' and y < 2:
        return (x, y+1)
    elif m == 'L' and x > 0:
        return (x-1, y)
    elif m == 'U' and y > 0:
        return (x, y-1)
    return x, y

def get_button(x,y):
    return str((y*3)+x+1)

keypad2 = [
    '..1..',
    '.234.',
    '56789',
    '.ABC.',
    '..D..',
]

def move_finger2(m, x, y):
    if m == 'R':
        nx, ny = x+1, y
    elif m == 'D':
        nx, ny = x, y+1
    elif m == 'L':
        nx, ny = x-1, y
    elif m == 'U':
        nx, ny = x, y-1

    if 0 <= nx < 5 and 0 <= ny < 5 and keypad2[ny][nx] != '.':
        return nx, ny

    return x, y


def part1(inp):
    x, y = 1, 1
    presses = []

    for line in inp.splitlines():
        for m in line:
            x,y = move_finger(m, x, y)
        button = get_button(x,y)
        presses.append(button)
    return ''.join(presses)


def part2(inp):
    x, y = 0, 2
    presses = []

    for line in inp.splitlines():
        for m in line:
            x,y = move_finger2(m, x, y)
        presses.append(keypad2[y][x])
    return ''.join(presses)
