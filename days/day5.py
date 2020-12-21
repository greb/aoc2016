import hashlib

def gen_hash(door, i):
    data = (door + str(i)).encode()
    return hashlib.md5(data).hexdigest()

def part1(inp):
    door = inp.strip()

    pw = []
    index = 0
    for _ in range(8):
        while True:
            h = gen_hash(door, index)
            if h.startswith('00000'):
                pw.append(h[5])
                break
            index += 1
        index += 1

    print(''.join(pw))


def part2(inp):
    door = inp.strip()

    pw = [None]*8
    index = 0
    cnt = 0
    while cnt < 8:
        h = gen_hash(door, index)
        if h.startswith('00000'):
            i, d = h[5], h[6]
            i = int(i) if i.isdigit() else None
            if i is not None and i < 8 and pw[i] is None:
                pw[i] = d
                cnt += 1
        index += 1

    return ''.join(pw)
