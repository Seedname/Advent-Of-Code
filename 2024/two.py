import read


def part_1(input: list[str]) -> int:
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
    return result


def part_2(input: list[str]) -> int:
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
        numbers = report.strip().split(" ")
        for i in range(len(numbers)):
            nums = numbers[:]
            nums.pop(i)
            if is_safe(' '.join(nums)):
                return True
        return False

    result = sum(is_fault_safe(report) for report in input)
    return result


if __name__ == "__main__":
    read.test_solution(2, 2024, part_1, part_2)
