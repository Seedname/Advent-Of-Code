import read


def part1(input: list[str]) -> None:
    def is_safe(report: str) -> bool:
        numbers = list(map(int, report.strip().split(" ")))
        sign = 0
        for i in range(len(numbers)-1):
            delta = numbers[i+1] - numbers[i]
            if delta == 0 or abs(delta) > 3:
                return False
            new_sign = delta / abs(delta)
            if sign != 0 and sign != new_sign:
                return False
            sign = new_sign
        return True

    result = sum(is_safe(report) for report in input)
    print(f"Part 1: {result}")


def part2(input: list[str]) -> None:
    def is_safe(report: str) -> bool:
        numbers = list(map(int, report.strip().split(" ")))
        sign = 0
        for i in range(len(numbers) - 1):
            delta = numbers[i + 1] - numbers[i]
            if delta == 0 or abs(delta) > 3:
                return False
            new_sign = delta / abs(delta)
            if sign != 0 and sign != new_sign:
                return False
            sign = new_sign
        return True

    def is_fault_safe(report: str) -> bool:
        if is_safe(report):
            return True
        numbers = list(map(int, report.strip().split(" ")))
        for i in range(len(numbers)):
            nums = numbers[:]
            nums.pop(i)
            if is_safe(' '.join(map(str, nums))):
                return True
        return False

    result = sum(is_fault_safe(report) for report in input)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    input = read.get_input(2, 2024)
    part1(input)
    part2(input)