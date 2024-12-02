import read
from collections import Counter


def part_1(input: list[str]) -> int:
    first_list = sorted(int(line.split("   ")[0]) for line in input)
    second_list = sorted(int(line.split("   ")[1]) for line in input)
    result = sum(abs(first - second) for first, second in zip(first_list, second_list))
    return result


def part_2(input: list[str]) -> int:
    first_list = (int(line.split("   ")[0]) for line in input)
    second_list_occurrences = Counter(int(line.split("   ")[1]) for line in input)
    result = sum(num * second_list_occurrences.get(num, 0) for num in first_list)
    return result


if __name__ == "__main__":
    read.test_solution(1, 2024, part_1, part_2)
