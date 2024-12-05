import read
from collections import defaultdict
from dataclasses import dataclass, field

@dataclass
class Page:
    next_numbers: list[int] = field(default_factory=lambda: [])


def part_1(input: list[str]) -> int:
    pages = defaultdict(Page)
    next_step = False

    result = 0
    for line in input:
        if line.strip() == "":
            next_step = True
            continue

        if not next_step:
            before, after = map(int, line.strip().split("|"))
            pages[before].next_numbers.append(after)
            continue

        order = list(map(int, line.strip().split(",")))
        for i in range(len(order)-1, 0, -1):
            current = order[i]
            previous = order[i-1]
            if current not in pages[previous].next_numbers:
                break
        else:
            middle_number = order[len(order)//2]
            result += middle_number

    return result


def part_2(input: list[str]) -> int:
    pages = defaultdict(Page)
    next_step = False

    def fix_order(order: list[int]) -> list[int]:
        for _ in range(len(order)):
            for i in range(len(order) - 1, 0, -1):
                current = order[i]
                previous = order[i-1]
                if current not in pages[previous].next_numbers:
                    order[i] = previous
                    order[i-1] = current
        return order


    result = 0
    for line in input:
        if line.strip() == "":
            next_step = True
            continue

        if not next_step:
            before, after = map(int, line.strip().split("|"))
            pages[before].next_numbers.append(after)
            continue

        order = list(map(int, line.strip().split(",")))
        for i in range(len(order)-1, 0, -1):
            current = order[i]
            previous = order[i-1]
            if current not in pages[previous].next_numbers:
                new_order = fix_order(order)
                result += new_order[len(new_order)//2]
                break
    return result


if __name__ == "__main__":
    read.test_solution(5, 2024, part_2)
