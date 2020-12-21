import re
import collections

def parse(inp):
    rooms = []
    for line in inp.splitlines():
        m = re.match(r'([a-z\-]+)\-(\d+)\[([a-z]+)\]', line)
        name, sector, checksum = m.groups()
        room = int(sector), name, checksum
        rooms.append(room)
    return rooms

def gen_checksum(name):
    cnt = collections.Counter(name.replace('-', ''))
    ranking = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))
    checksum = ''.join(r[0] for r in ranking[:5])
    return checksum

def decrypt(sector, name):
    buf = []
    for ch in name:
        if ch == '-':
            buf.append(' ')
            continue

        pos = ord(ch) - ord('a')
        pos = (pos + sector) % 26
        ch  = chr(ord('a') + pos)
        buf.append(ch)
    return ''.join(buf)

def part1(inp):
    rooms = parse(inp)

    total = 0
    for sector, name, checksum in rooms:
        if gen_checksum(name) == checksum:
            total += sector
    return total


def part2(inp):
    rooms = parse(inp)

    for sector, name, _ in rooms:
        name = decrypt(sector, name)
        if name == 'northpole object storage':
            return sector

