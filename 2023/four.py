import read


def part1(input: list[str]) -> None:
    total = 0
    for line in input:
        _, card = line.split(": ")

        winning, numbers = card.strip().split(" | ")

        winning = set(map(int, filter(lambda x: x.strip() != "", winning.strip().split(" "))))
        numbers = list(map(int, filter(lambda x: x.strip() != "", numbers.strip().split(" "))))

        current = 0
        for number in numbers:
            if number in winning:
                if current == 0:
                    current = 1
                else:
                    current <<= 1

        total += current
    print(f"Part 1: {total}")


def part2(input: list[str]) -> None:
    total = 0
    duplicates = list([1] * len(input))
    for i in range(len(input)):
        line = input[i]
        _, card = line.split(": ")

        winning, numbers = card.strip().split(" | ")

        winning = set(map(int, filter(lambda x: x.strip() != "", winning.strip().split(" "))))
        numbers = list(map(int, filter(lambda x: x.strip() != "", numbers.strip().split(" "))))

        current = sum(number in winning for number in numbers)

        for j in range(i+1, min(len(input), i+current+1)):
            duplicates[j] += duplicates[i]

        total += duplicates[i]

    print(f"Part 2: {total}")


if __name__ == '__main__':
    input = read.load_input(4, 2023)
    part1(input)
    part2(input)