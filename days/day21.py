import itertools

def swap_pos(s, x, y):
    l = list(s)
    l[x], l[y] = l[y], l[x]
    return ''.join(l)

def swap_letter(s, x, y):
    idx_x = s.find(x)
    idx_y = s.find(y)
    return swap_pos(s, idx_x, idx_y)

def rotate_left(s, x):
    x = x % len(s)
    return s[x:] + s[:x]

def rotate_right(s, x):
    x = x % len(s)
    return s[-x:] + s[:-x]

def rotate_letter(s, x):
    idx = s.find(x)
    if idx >= 4:
        idx += 2
    else:
        idx += 1
    return rotate_right(s, idx)

def reverse_pos(s, x, y):
    return s[:x] + ''.join(reversed(s[x:y+1])) + s[y+1:]

def move_pos(s, x, y):
    l = list(s)
    c = l.pop(x)
    l.insert(y, c)
    return ''.join(l)

def parse(inp):
    instrs = []
    for line in inp.splitlines():
        words = line.split()
        if words[0] == 'swap':
            if words[1] == 'position':
                instr = (swap_pos, int(words[2]), int(words[5]))
            else:
                instr = (swap_letter, words[2], words[5])
        elif words[0] == 'rotate':
            if words[1] == 'left':
                instr = (rotate_left, int(words[2]))
            elif words[1] == 'right':
                instr = (rotate_right, int(words[2]))
            else:
                instr = (rotate_letter, words[6])
        elif words[0] == 'reverse':
            instr = (reverse_pos, int(words[2]), int(words[4]))
        elif words[0] == 'move':
            instr = (move_pos, int(words[2]), int(words[5]))
        instrs.append(instr)
    return instrs

def part1(inp):
    instrs = parse(inp)

    s = 'abcdefgh'
    for f, *args in instrs:
        s = f(s, *args)
    return s


def part2(inp):
    instrs = parse(inp)

    target = 'fbgdceah'
    for comb in itertools.permutations('abcdefgh'):
        s = ''.join(comb)
        for f, *args in instrs:
            s = f(s, *args)
        if s == target:
            return ''.join(comb)

import unittest
class Test(unittest.TestCase):
    def test_str_functions(self):
        s = 'abcde'

        s = swap_pos(s, 4, 0)
        self.assertEqual(s, 'ebcda')

        s = swap_letter(s, 'd', 'b')
        self.assertEqual(s, 'edcba')

        s = reverse_pos(s, 0, 4)
        self.assertEqual(s, 'abcde')

        s = rotate_left(s, 1)
        self.assertEqual(s, 'bcdea')

        s = move_pos(s, 1, 4)
        self.assertEqual(s, 'bdeac')

        s = move_pos(s, 3, 0)
        self.assertEqual(s, 'abdec')

        s = rotate_letter(s, 'b')
        self.assertEqual(s, 'ecabd')

        s = rotate_letter(s, 'd')
        self.assertEqual(s, 'decab')
