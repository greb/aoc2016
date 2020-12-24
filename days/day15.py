from pprint import pprint

def parse(inp):
    discs = []
    for line in inp.splitlines():
        words = line.split()
        n_pos = int(words[3])
        s_pos = int(words[11][:-1])
        discs.append( (n_pos, s_pos) )
    return discs

def drop_timing(discs):
    start = 0
    step = 1

    for i, disc in enumerate(discs):
        falltime = i+1
        n_pos, s_pos= disc
        while (start + falltime + s_pos) % n_pos:
            start += step
        step *= n_pos

    return start


def part1(inp):
    discs = parse(inp)
    return drop_timing(discs)


def part2(inp):
    discs = parse(inp)
    discs.append( (11, 0) )
    return drop_timing(discs)

