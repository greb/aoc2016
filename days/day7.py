import re

def is_abba(seg):
    match = re.match(r'.*(.)(.)\2\1.*', seg)
    if match:
        a, b = match.groups()
        return a != b
    return False

def tls_supported(ip):
    supernet = []
    hypernet = []

    for i, seg in enumerate(re.split(r'[\[\]]', ip)):
        p = is_abba(seg)
        if i % 2 == 0:
            supernet.append(p)
        else:
            hypernet.append(p)

    return any(supernet) and not any(hypernet)

def find_all_aba(seg):
    found = []
    start = 0
    pattern = re.compile(r'(.)(.)\1')
    while m := pattern.search(seg, start):
        a, b = m.groups()
        start = m.start() + 1
        if a != b:
            found.append( (a, b) )
    return found

def ssl_supported(ip):
    supernet = []
    hypernet = []

    for i, seg in enumerate(re.split(r'[\[\]]', ip)):
        if i % 2 == 0:
            supernet.extend(find_all_aba(seg))
        else:
            hypernet.extend(find_all_aba(seg))

    for aba in supernet:
        bab = aba[1], aba[0]
        if bab in hypernet:
            return True

    return False

def part1(inp):
    cnt = 0
    for ip in inp.splitlines():
        if tls_supported(ip):
            cnt += 1
    return cnt

def part2(inp):
    cnt = 0
    for ip in inp.splitlines():
        if ssl_supported(ip):
            cnt += 1
    return cnt

import unittest
class Test(unittest.TestCase):
    def test_is_abba(self):
        self.assertTrue( is_abba('abba') )
        self.assertFalse( is_abba('aaaa') )
        self.assertTrue( is_abba('ioxxoj') )
        self.assertFalse( is_abba('asdfgh') )

    def test_tls_supported(self):
        self.assertTrue( tls_supported('abba[mnop]qrst') )
        self.assertFalse( tls_supported('abcd[bddb]xyyx') )
        self.assertTrue( tls_supported('ioxxoj[asdfgh]zxcvbn') )

    def test_find_all_aba(self):
        target = [('z', 'a'), ('z', 'b')]
        self.assertEqual( find_all_aba('zazbz'), target )

        target = []
        self.assertEqual( find_all_aba('aaa'), [])

        target = []
        self.assertEqual( find_all_aba('xyz'), [])

    def test_ssl_supported(self):
        self.assertTrue( ssl_supported('aba[bab]xyz') )
        self.assertFalse( ssl_supported('xyx[xyx]xyx') )
        self.assertTrue( ssl_supported('aaa[kek]eke') )
        self.assertTrue( ssl_supported('zazbz[bzb]cdb') )

