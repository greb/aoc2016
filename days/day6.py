import collections

def part1(inp):
    lines = inp.splitlines()
    message = []

    for col in range(len(lines[0])):
        letters = (line[col] for line in lines)
        cnt = collections.Counter(letters)
        ch, _ = cnt.most_common(1)[0]
        message.append(ch)

    return ''.join(message)


def part2(inp):
    lines = inp.splitlines()
    message = []

    for col in range(len(lines[0])):
        letters = (line[col] for line in lines)
        cnt = collections.Counter(letters)
        ch, _ = cnt.most_common()[-1]
        message.append(ch)

    return ''.join(message)
