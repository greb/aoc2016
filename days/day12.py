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
        op, *args = self.code[self.counter]
        op = getattr(self, f'op_{op}')
        op(*args)

    def op_cpy(self, src, dst):
        if src.isdigit():
            val = int(src)
        else:
            val = self.regs[src]
        self.regs[dst] = val
        self.counter += 1

    def op_inc(self, reg):
        self.regs[reg] += 1
        self.counter += 1

    def op_dec(self, reg):
        self.regs[reg] -= 1
        self.counter += 1

    def op_jnz(self, src, offset):
        if src.isdigit():
            val = int(src)
        else:
            val = self.regs[src]
        if val != 0:
            self.counter += int(offset)
        else:
            self.counter += 1


def part1(inp):
    c = Computer(inp)

    while c.counter < len(c.code):
        c.step()

    return c.regs['a']

def part2(inp):
    c = Computer(inp)
    c.regs['c'] = 1
    while c.counter < len(c.code):
        c.step()
    return c.regs['a']
