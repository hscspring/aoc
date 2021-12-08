import pnlp

file_name = "day2.txt"
file_name = "day2_input1.txt"
lines = pnlp.read_lines(file_name)


def part1(lines):
    x = []
    y = []
    for v in lines:
        key, step = v.split()
        k = int(step)
        if key == "forward":
            x.append(k)
        elif key == "up":
            y.append(-k)
        elif key == "down":
            y.append(k)
    xs = sum(x)
    ys = sum(y)
    print(xs * ys)


def part2(lines):
    x, y = [], []
    aim = 0
    for v in lines:
        key, step = v.split()
        k = int(step)
        if key == "forward":
            x.append(k)
            yk = aim * k
            y.append(yk)
        elif key == "up":
            aim -= k
        elif key == "down":
            aim += k
    xs = sum(x)
    ys = sum(y)
    print(xs * ys)


part1(lines)
part2(lines)
