import read
from collections import Counter


def part1(input: list[str]) -> None:
    first_list = sorted(int(line.split("   ")[0]) for line in input)
    second_list = sorted(int(line.split("   ")[1]) for line in input)
    result = sum(abs(first - second) for first, second in zip(first_list, second_list))
    print(f"Part 1: {result}")


def part2(input: list[str]) -> None:
    first_list = (int(line.split("   ")[0]) for line in input)
    second_list_occurrences = Counter(int(line.split("   ")[1]) for line in input)
    result = sum(num * second_list_occurrences.get(num, 0) for num in first_list)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    input = read.get_input(1, 2024)

    part1(input)
    part2(input)
