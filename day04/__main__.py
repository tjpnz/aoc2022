from dataclasses import dataclass
from typing import Tuple

from util import aoc_input


@dataclass
class Range:
    start: int
    end: int

    def contains(self, other: "Range") -> bool:
        return self.start <= other.start and self.end >= other.end

    def overlaps(self, other: "Range") -> bool:
        return self.contains(other) or \
               self.start >= other.start and self.start <= other.end and self.end >= other.end or \
               self.start <= other.start and self.end >= other.start and self.end <= other.end


def get_range_pair(line: str) -> Tuple[Range, Range]:
    a, b = line.strip().split(",")
    a1, a2 = a.split("-")
    b1, b2 = b.split("-")
    return Range(int(a1), int(a2)), Range(int(b1), int(b2)),


def problem1() -> int:
    count = 0
    for line in aoc_input("input.txt"):
        r1, r2 = get_range_pair(line)
        if r1.contains(r2) or r2.contains(r1):
            count += 1
    return count


def problem2() -> int:
    count = 0
    for line in aoc_input("input.txt"):
        r1, r2 = get_range_pair(line)
        if r1.overlaps(r2) or r2.overlaps(r1):
            count += 1
    return count


print(problem1())
print(problem2())
