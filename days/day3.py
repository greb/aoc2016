def parse(inp):
    triangles = []
    for line in inp.splitlines():
        sides = [int(l) for l in line.split()]
        triangles.append(sides)
    return triangles

def check_triangles(triangles):
    cnt = 0
    for sides in triangles:
        a,b,c = sides
        if a+b > c and a+c > b and b+c > a:
            cnt += 1
    return cnt

def part1(inp):
    triangles = parse(inp)
    return check_triangles(triangles)

def part2(inp):
    triangles = parse(inp)
    triangles2 = []
    for i in range(0, len(triangles), 3):
        chunk = triangles[i:i+3]
        chunk = [list(seg) for seg in zip(*chunk)]
        triangles2.extend(chunk)
    return check_triangles(triangles2)
