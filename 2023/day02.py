import read


def part_1(input: list[str]) -> int:
    sum_ids = 0

    mappings = {"red": 12,
                "green": 13,
                "blue": 14}

    for line in input:
        game, values = line.split(":")
        subsets = values.strip().split("; ")
        possible = True

        for subset in subsets:
            items = subset.split(", ")
            for item in items:
                amount, category = item.split(" ")
                if int(amount) > mappings[category]:
                    possible = False
                    break

                if not possible: break
            if not possible: break

        if possible:
            _, cid = game.split(" ")
            sum_ids += int(cid)

    return sum_ids


def part_2(input: list[str]) -> int:
    sum_power = 0

    for line in input:
        game, values = line.split(":")
        subsets = values.strip().split("; ")

        mappings = {"red": 0,
                    "green": 0,
                    "blue": 0}

        for subset in subsets:
            items = subset.split(", ")
            for item in items:
                amount, category = item.split(" ")
                mappings[category] = max(mappings[category], int(amount))

        sum_power += mappings["red"] * mappings["green"] * mappings["blue"]

    return sum_power


if __name__ == "__main__":
    read.test_solution(2, 2023, part_1, part_2)
