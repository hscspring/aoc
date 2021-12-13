from dataclasses import dataclass
import pnlp

file_name = "data/day4_input1.txt"
file_name = "data/day4.txt"


@dataclass
class Ele:

    x: int
    y: int
    val: int
    marked: bool


def preprocess(file_name):
    lines = pnlp.read_lines(file_name)
    nums = list(map(int, lines[0].split(",")))
    arrs = [v.strip() for v in lines[1:]]
    ret = []
    tmp = []
    i = 0
    iy = 0
    for _, arr in enumerate(arrs):
        ix = 0
        for _, v in enumerate(arr.split()):
            v = int(v)
            x = iy
            y = ix
            it = Ele(x, y, v, False)
            tmp.append(it)
            ix += 1
        i += 1
        iy += 1
        if i % 5 == 0:
            ret.append(tmp)
            tmp = []
            iy = 0
    return nums, ret


def check_marked(eles):
    ret = []
    for ida, arr in enumerate(eles):
        for idl, line in enumerate(arr):
            marked = True
            for i, v in enumerate(line):
                if not v.marked:
                    marked = False
                    break
            if marked:
                ret.append((ida, idl, i))
    return ret


def mark(n, arrs):
    for arr in arrs:
        for line in arr:
            for v in line:
                if v.val == n:
                    v.marked = True


def calc(arrs, marked, add):
    ret = []
    for m in marked:
        ida, idl, i = m
        lines = arrs[ida][idl]
        loc = arrs[ida][idl][i].val
        marked_sum = sum(v.val for v in lines)
        score = (add - marked_sum) * loc
        ret.append(score)
    return ret


def calc_sum(arrs):
    i = 0
    for arr in arrs:
        for line in arr:
            for v in line:
                i += v.val
    return i


def part1(file_name):
    nums, arrs = preprocess(file_name)
    add = calc_sum(arrs)
    for n in nums:
        mark(n, arrs)
        marked = check_marked(arrs)
        if marked:
            ret = calc(arrs, marked, add)
            print(ret)
            break


def part2(lines):
    ...


part1(file_name)
print("=" * 50)
part2(file_name)
