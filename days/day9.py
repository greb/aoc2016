import re

marker_pat = re.compile(r'\((\d+)x(\d+)\)')

def decompress_length(data):
    length = 0

    while m := marker_pat.search(data):
        # Front part
        length += m.start()
        end = m.end()

        # Compressed part
        comp_length, repeats = int(m[1]), int(m[2])
        length += comp_length * repeats

        data = data[end+comp_length:]

    # Tail of data
    length += len(data)
    return length


def decompress_length_ver2(data):
    length = 0

    while m := marker_pat.search(data):
        length += m.start()
        end = m.end()

        # Compressed part
        comp_length, repeats = int(m[1]), int(m[2])
        compressed = data[end:end+comp_length]
        length += decompress_length_ver2(compressed) * repeats

        data = data[end+comp_length:]

    length += len(data)
    return length

def part1(inp):
    data = inp.strip()
    return decompress_length(data)

def part2(inp):
    data = inp.strip()
    return decompress_length_ver2(data)

import unittest
class Test(unittest.TestCase):
    def test_decompress(self):
        f = decompress_length
        self.assertEqual( f('ADVENT'), 6)
        self.assertEqual( f('A(1x5)BC'), 7)
        self.assertEqual( f('(3x3)XYZ'), 9)
        self.assertEqual( f('A(2x2)BCD(2x2)EFG'), 11)
        self.assertEqual( f('(6x1)(1x3)A'), 6)
        self.assertEqual( f('X(8x2)(3x3)ABCY'), 18)

    def test_decompress_ver2(self):
        f = decompress_length_ver2
        self.assertEqual( f('(3x3)XYZ'), len('XYZXYZXYZ'))
        self.assertEqual( f('X(8x2)(3x3)ABCY'),
                len('XABCABCABCABCABCABCY'))
        self.assertEqual( f('(27x12)(20x12)(13x14)(7x10)(1x12)A'), 241920)
        self.assertEqual(
                f('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'),
                445)
