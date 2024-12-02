import string
import read


def part_1(input: list[str]) -> int:
    NON_SYMBOLS = set("0123456789.")
    NUMERIC = set(string.digits)
    visited = set()

    def get_adjacent_numbers(k: int, l: int) -> list[int]:
        nums = []
        for i in range(-1, 2):
            row = k + i
            if row < 0 or row >= len(input): continue
            for j in range(-1, 2):
                col = l + j
                if col < 0 or col >= len(input[i]): continue
                if i == 0 and j == 0: continue
                if input[row][col] not in NUMERIC: continue

                pointer1 = col
                pointer2 = col + 1
                discard = False

                while pointer1 >= 0 and input[row][pointer1] in NUMERIC:
                    if (row, pointer1) in visited:
                        discard = True
                        break
                    visited.add((row, pointer1))
                    pointer1 -= 1

                if discard: continue

                while pointer2 < len(input) and input[row][pointer2] in NUMERIC:
                    if (row, pointer2) in visited:
                        discard = True
                        break
                    visited.add((row, pointer2))
                    pointer2 += 1

                if not discard:
                    nums.append(int(input[row][pointer1+1:pointer2]))
        return nums

    total = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] not in NON_SYMBOLS:
                total += sum(get_adjacent_numbers(i, j))

    return total


def part_2(input: list[str]) -> int:
    NON_SYMBOLS = set("0123456789.")
    NUMERIC = set(string.digits)
    visited = set()

    def get_adjacent_gear_ratio(k: int, l: int) -> int:
        nums = []
        for i in range(-1, 2):
            row = k + i
            if row < 0 or row >= len(input): continue
            for j in range(-1, 2):
                col = l + j
                if col < 0 or col >= len(input[i]): continue
                if i == 0 and j == 0: continue
                if input[row][col] not in NUMERIC: continue

                pointer1 = col
                pointer2 = col + 1
                discard = False

                while pointer1 >= 0 and input[row][pointer1] in NUMERIC:
                    if (row, pointer1) in visited:
                        discard = True
                        break
                    visited.add((row, pointer1))
                    pointer1 -= 1

                if discard: continue

                while pointer2 < len(input) and input[row][pointer2] in NUMERIC:
                    if (row, pointer2) in visited:
                        discard = True
                        break
                    visited.add((row, pointer2))
                    pointer2 += 1

                if not discard:
                    nums.append(int(input[row][pointer1+1:pointer2]))

        if len(nums) == 1:
            return 0

        prod = 1
        for num in nums:
            prod *= num

        return prod

    total = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] not in NON_SYMBOLS:
                total += get_adjacent_gear_ratio(i, j)

    return total


if __name__ == "__main__":
    read.test_solution(3, 2023, part_1, part_2)
