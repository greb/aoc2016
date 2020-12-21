import re

WIDTH, HEIGHT = 50, 6

def make_screen(w, h):
    return [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]

def display_screen(screen):
    for line in screen:
        print(''.join(line))

def apply_instr(screen, instr):
    op, *args = instr

    if op == 'rect':
        apply_rect(screen, *args)
    elif op == 'col':
        apply_col(screen, *args)
    elif op == 'row':
        apply_row(screen, *args)

def apply_rect(screen, w, h):
    for y in range(h):
        for x in range(w):
            screen[y][x] = '#'

def apply_col(screen, x, v):
    old_col = [screen[y][x] for y in range(HEIGHT)]

    for y in range(HEIGHT):
        yn = (y + v) % HEIGHT
        screen[yn][x] = old_col[y]

def apply_row(screen, y, v):
    old_row = [screen[y][x] for x in range(WIDTH)]

    for x in range(WIDTH):
        xn = (x + v) % WIDTH
        screen[y][xn] = old_row[x]


def parse(inp):
    pat_rect = re.compile(r'rect (\d+)x(\d+)')
    pat_col  = re.compile(r'rotate column x=(\d+) by (\d+)')
    pat_row  = re.compile(r'rotate row y=(\d+) by (\d+)')

    instrs = []
    for line in inp.splitlines():
        if m := pat_rect.match(line):
            instr = ('rect', int(m[1]), int(m[2]))
        elif m := pat_col.match(line):
            instr = ('col', int(m[1]), int(m[2]))
        elif m := pat_row.match(line):
            instr = ('row', int(m[1]), int(m[2]))
        else:
            continue
        instrs.append(instr)
    return instrs

def part1(inp):
    instrs = parse(inp)

    screen = make_screen(WIDTH, HEIGHT)
    for instr in instrs:
        apply_instr(screen, instr)

    return sum(screen[y][x]=='#' for y in range(HEIGHT) for x in range(WIDTH))

def part2(inp):
    instrs = parse(inp)

    screen = make_screen(WIDTH, HEIGHT)
    for instr in instrs:
        apply_instr(screen, instr)

    display_screen(screen)
    return "Look at the screen for solution"
