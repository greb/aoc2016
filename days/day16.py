def gen_curve(a, min_len):
    while len(a) < min_len:
        b = ['10'[int(c)] for c in reversed(a)]
        a = a + '0' + ''.join(b)
    return a[:min_len]

def gen_chksum(a):
    while len(a) % 2 == 0:
        new_a = []
        for i in range(0, len(a), 2):
            chunk = a[i:i+2]
            if chunk in ('00', '11'):
                new_a.append('1')
            elif chunk in ('01', '10'):
                new_a.append('0')
        a = ''.join(new_a)
    return a

def part1(inp):
    a = inp.strip()
    min_len = 272
    a = gen_curve(a, min_len)
    a = gen_chksum(a)
    return a


def part2(inp):
    a = inp.strip()

    min_len = 35651584
    a = gen_curve(a, min_len)
    a = gen_chksum(a)
    return a
