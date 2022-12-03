from collections import defaultdict

from util import aoc_input

priorities = {}
for _i, ch in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    priorities[ch] = _i + 1


def problem1():
    total = 0

    for line in aoc_input("input.txt"):
        items = list(line.strip())

        c1 = defaultdict(lambda: 0)
        for i in range(len(items)//2):
            c1[items[i]] += 1
        c2 = defaultdict(lambda: 0)
        for i in range(len(items)//2, len(items)):
            c2[items[i]] += 1

        in_both = list(set(c1.keys()) & set(c2.keys()))[0]
        total += priorities[in_both]

    return total


def problem2():
    total = 0

    curr_group = []
    groups = []
    for line in aoc_input("input.txt"):
        items = set(list(line.strip()))
        curr_group.append(items)
        if len(curr_group) == 3:
            groups.append(curr_group)
            curr_group = []
    for e1, e2, e3 in groups:
        total += priorities[list(e1 & e2 & e3)[0]]

    return total


print(problem1())
print(problem2())
