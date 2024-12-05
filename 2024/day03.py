import read
import re


def part_1(input: list[str]) -> int:
    matches = re.findall("mul\((\d+),(\d+)\)", ''.join(input))
    sum = 0
    for match in matches:
        first, second = map(int, match)
        sum += first * second
    return sum


def part_2(input: list[str]) -> int:
    matches = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", ''.join(input))
    sum = 0
    enabled = True
    for match in matches:
        if 'do()' == match:
            enabled = True
        elif "don't()" == match:
            enabled = False
        elif enabled:
            num1, num2 = map(int, re.search("mul\((\d+),(\d+)\)", match).groups())
            sum += num1 * num2

    return sum


if __name__ == "__main__":
    read.test_solution(3, 2024, part_1, part_2)
