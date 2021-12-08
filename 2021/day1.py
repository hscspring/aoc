import pnlp

lines = pnlp.read_lines("day1_input1.txt")
lines = list(map(int, lines))


def part1(lines):
    n = 0
    prev = 1e10
    for i in lines:
        if i > prev:
            n += 1
        prev = i
    print(n)


def part2(lines):
    new = []
    length = len(lines)
    for i in range(length - 2):
        part = lines[i:i + 3]
        add = sum(part)
        new.append(add)
    part1(new)


part1(lines)
part2(lines)
