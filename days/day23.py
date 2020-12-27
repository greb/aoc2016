import pprint

tgl = {
    'inc': 'dec',
    'dec': 'inc',
    'tgl': 'inc',
    'cpy': 'jnz',
    'jnz': 'cpy',
}
class Computer():
    def __init__(self, code):
        self.regs = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
        }
        self.counter = 0
        self.code = [line.split() for line in code.splitlines()]

    def step(self):
        #optimize
        if 4 <= self.counter <=9:
            if self.counter == 4:
                self.regs['a'] += self.regs['b']*self.regs['d']
                self.regs['c'] = 0
                self.regs['d'] = 0
                self.counter = 10
            else:
                self.counter += 1
            return

        op, *args = self.code[self.counter]
        op = getattr(self, f'op_{op}')
        op(*args)

    def op_inc(self, reg):
        if reg in self.regs:
            self.regs[reg] += 1
        self.counter += 1

    def op_dec(self, reg):
        if reg in self.regs:
            self.regs[reg] -= 1
        self.counter += 1

    def op_cpy(self, src, dst):
        if src in self.regs:
            val = self.regs[src]
        else:
            val = int(src)

        if dst in self.regs:
            self.regs[dst] = val
        self.counter += 1

    def op_jnz(self, src, offset):
        if src in self.regs:
            val = self.regs[src]
        else:
            val = int(src)

        if offset in self.regs:
            offset = self.regs[offset]
        else:
            offset = int(offset)

        if val != 0:
            self.counter += offset
        else:
            self.counter += 1

    def op_tgl(self, offset):
        if offset in self.regs:
            offset = self.regs[offset]
        else:
            offset = int(offset)

        idx = self.counter + offset
        if idx < len(self.code):
            instr = self.code[idx]
            instr[0] = tgl[instr[0]]
        self.counter += 1

def part1(inp):
    c = Computer(inp)

    c.regs['a'] = 7
    while c.counter < len(c.code):
        c.step()

    return c.regs['a']

def part2(inp):
    c = Computer(inp)

    c.regs['a'] = 12
    while c.counter < len(c.code):
        c.step()

    return c.regs['a']

