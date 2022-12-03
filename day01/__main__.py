import heapq

from util import aoc_input


def problem1():
    curr = 0
    max_so_far = 0
    for line in aoc_input("input.txt"):
        line = line.strip()
        if line == "":
            max_so_far = max(max_so_far, curr)
            curr = 0
        else:
            curr += int(line)

    return max_so_far


def problem2():
    curr = 0
    heap = []
    for line in aoc_input("input.txt"):
        line = line.strip()
        if line == "":
            heapq.heappush(heap, -curr)
            curr = 0
        else:
            curr += int(line)

    top_three_sum = -heapq.heappop(heap) + -heapq.heappop(heap) + -heapq.heappop(heap)
    return top_three_sum


print(problem1())
print(problem2())

