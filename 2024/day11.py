import read


def part_1(input: list[str]) -> int:
    stones = list(map(int, input[0].strip().split(" ")))
    for _ in range(25):
        new_stones = []
        for i, stone in enumerate(stones):
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                new_stone = str(stone)
                midpoint = len(str(stone)) // 2
                new_stones.append(int(f'{new_stone[:midpoint]}'))
                new_stones.append(int(f'{new_stone[midpoint:]}'))
            else:
                new_stones.append(stones[i] * 2024)
        stones = new_stones
    return len(stones)


def part_2(input: list[str]) -> int:
    stones = list(map(int, input[0].strip().split(" ")))
    from functools import cache
    @cache
    def get_stone_count(stone, n):
        if n == 0: return 1

        if stone == 0:
            return get_stone_count(1, n - 1)
        elif len(str(stone)) % 2 == 0:
            new_stone = str(stone)
            midpoint = len(str(stone)) // 2
            return get_stone_count(int(f'{new_stone[:midpoint]}'), n - 1) + get_stone_count(int(f'{new_stone[midpoint:]}'), n - 1)
        else:
            return get_stone_count(stone * 2024, n - 1)

    total = sum(get_stone_count(stone, 75) for stone in stones)
    return total


if __name__ == "__main__":
    test = read.load_input(11, 2024)
    print(part_2(test))
