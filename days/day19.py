class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None
        self.prv = None

    def delete(self):
        self.prv.nxt = self.nxt
        self.nxt.prv = self.prv

def build_elf_list(n):
    elfs = [Node(v) for v in range(n)]
    for i in range(n):
        elfs[i].nxt = elfs[(i+1)%n]
        elfs[i].prv = elfs[(i-1)%n]
    return elfs

def part1(inp):
    n = int(inp.strip())
    elfs = build_elf_list(n)

    elf = elfs[0]
    for i in range(n-1):
        elf.nxt.delete()
        elf = elf.nxt
    return elf.val + 1

def part2(inp):
    n = int(inp.strip())
    elfs = build_elf_list(n)

    elf = elfs[0]
    across = elfs[n//2]
    for i in range(n-1):
        across.delete()
        across = across.nxt
        if (n-i) % 2 == 1:
            across = across.nxt
        elf = elf.nxt
    return elf.val + 1 
