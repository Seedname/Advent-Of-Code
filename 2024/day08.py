import read
from collections import defaultdict
from itertools import combinations


def part_1(input: list[str]) -> int:
    groups = defaultdict(list)
    input = [list(line) for line in input]

    for j, line in enumerate(input):
        for i, char in enumerate(line):
            if char == ".": continue
            groups[char].append((i, j))

    def in_bounds(x, y):
        return x >= 0 and y >= 0 and x < len(input) and y < len(input[0])

    for char in groups:
        two_combs = combinations(groups[char], 2)
        for comb in two_combs:
            first, second = comb
            if first == second: continue

            x1, y1 = first
            x2, y2 = second

            x3, y3 = x2 + (x2 - x1), y2 + (y2 - y1)
            x4, y4 = x1 - (x2 - x1), y1 - (y2 - y1)

            if in_bounds(x3, y3):
                input[y3][x3] = "#"

            if in_bounds(x4, y4):
                input[y4][x4] = "#"

    return sum(line.count("#") for line in input)


def part_2(input: list[str]) -> int:
    groups = defaultdict(list)
    input = [list(line) for line in input]

    for j, line in enumerate(input):
        for i, char in enumerate(line):
            if char == ".": continue
            groups[char].append((i, j))

    def in_bounds(x, y):
        return x >= 0 and y >= 0 and x < len(input) and y < len(input[0])

    for char in groups:
        two_combs = combinations(groups[char], 2)
        for comb in two_combs:
            first, second = comb
            if first == second: continue

            x1, y1 = first
            x2, y2 = second

            x3, y3 = x2 + (x2 - x1), y2 + (y2 - y1)
            while in_bounds(x3, y3):
                if input[y3][x3] == ".":
                    input[y3][x3] = "#"
                x3 += (x2 - x1)
                y3 += (y2 - y1)

            x4, y4 = x1 - (x2 - x1), y1 - (y2 - y1)
            while in_bounds(x4, y4):
                if input[y4][x4] == ".":
                    input[y4][x4] = "#"
                x4 -= (x2 - x1)
                y4 -= (y2 - y1)

    return sum(line.count("#") for line in input) + sum(len(groups[group]) for group in groups)


if __name__ == "__main__":
    read.test_solution(8, 2024, part_1, part_2)
