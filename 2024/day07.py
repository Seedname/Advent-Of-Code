import read
import math


def part_1(input: list[str]) -> int:
    def is_valid(line: str) -> int:
        test_num, nums = line.split(": ")
        test_num = int(test_num)
        nums = list(map(int, nums.strip().split(" ")))

        for i in range(2 ** (len(nums)-1)+1):
            result = nums[0]
            for j in range(1, len(nums)):
                if i % 2 == 0:
                    result += nums[j]
                else:
                    result *= nums[j]
                i //= 2

            if result == test_num:
                return test_num

        return 0

    return sum(is_valid(line) for line in input)


def part_2(input: list[str]) -> int:
    def is_valid(line: str) ->  int:
        test_num, nums = line.split(": ")
        test_num = int(test_num)
        nums = list(map(int, nums.strip().split(" ")))

        for i in range(3 ** (len(nums)-1)+1):
            result = nums[0]
            for j in range(1, len(nums)):
                if i % 3 == 0:
                    result += nums[j]
                elif i % 3 == 1:
                    result *= nums[j]
                else:
                    result *= pow(10, int(math.log10(nums[j])) + 1)
                    result += nums[j]

                i //= 3

            if result == test_num:
                return test_num

        return 0

    return sum(is_valid(line) for line in input)


if __name__ == "__main__":
    day = 7
    read.test_solution(day, 2024, part_1, part_2)
