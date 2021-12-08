import pnlp
import copy
from collections import Counter

file_name = "day3_input1.txt"
# file_name = "day3.txt"
lines = pnlp.read_lines(file_name)


def part1(lines):
    most, least = [], []
    length = len(lines[0])
    for i in range(length):
        tmp = [v[i] for v in lines]
        count = Counter(tmp).most_common()
        most.append(count[0][0])
        least.append(count[1][0])
    gamma = int("".join(most), 2)
    epsilon = int("".join(least), 2)
    print(gamma * epsilon)


def remove_with_idx(data, i, type):
    new = []
    tmp = [v[i] for v in data]
    count = Counter(tmp).most_common()
    if count[0][1] == count[1][1]:
        if type == "most":
            flag = "1"
        else:
            flag = "0"
    else:
        if type == "most":
            idx = 0
        else:
            idx = 1
        flag = count[idx][0]
    for k, v in enumerate(data):
        if v[i] != flag:
            continue
        new.append(v)
    return new


def help2(lines, type):
    data = copy.deepcopy(lines)
    i = 0
    while len(data) > 1:
        data = remove_with_idx(data, i, type)
        i += 1
    ret = int(data[0], 2)
    return ret


def part2(lines):
    oxygen = help2(lines, "most")
    co2 = help2(lines, "least")
    print(oxygen * co2)


part1(lines)
print("=" * 50)
part2(lines)
