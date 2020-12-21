from collections import defaultdict
from pprint import pprint

def parse(inp):
    inputs = []
    outputs = {}

    for line in inp.splitlines():
        words = line.split()
        if words[0] == 'value':
            robot, value = int(words[5]), int(words[1])
            inputs.append( (robot, value) )
        else:
            robot = int(words[1])
            lo = words[5], int(words[6])
            hi = words[10], int(words[11])
            outputs[robot] = lo, hi
    return inputs, outputs


def distribute_chips(inputs, outputs):
    bin_chips  = defaultdict()
    robot_chips = defaultdict(list)
    robot_stack = []

    for robot, value in inputs:
        robot_chips[robot].append(value)
        if len(robot_chips[robot]) == 2:
            robot_stack.append(robot)

    while robot_stack:
        robot = robot_stack.pop()
        chips = robot_chips[robot]

        lo, hi = outputs[robot]
        lo_chip = min(chips)
        hi_chip = max(chips)

        tgt, out = lo
        if tgt == 'bot':
            robot_chips[out].append(lo_chip)
            if len(robot_chips[out]) == 2:
                robot_stack.append(out)
        else:
            bin_chips[out] = lo_chip

        tgt, out = hi
        if tgt == 'bot':
            robot_chips[out].append(hi_chip)
            if len(robot_chips[out]) == 2:
                robot_stack.append(out)
        else:
            bin_chips[out] = hi_chip

    return robot_chips, bin_chips

def part1(inp):
    inputs, outputs = parse(inp)
    robot_chips, _ = distribute_chips(inputs, outputs)

    for robot, chips in robot_chips.items():
        if set(chips) == set([61, 17]):
            return robot

def part2(inp):
    inputs, outputs = parse(inp)
    robot_chips, _ = distribute_chips(inputs, outputs)

    _, bin_chips = distribute_chips(inputs, outputs)
    return bin_chips[0] * bin_chips[1] * bin_chips[2]
