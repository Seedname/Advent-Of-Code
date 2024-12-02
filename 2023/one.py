import read


def part1(input: list[str]) -> None:
    def get_calibration_value(string: str) -> int:
        numbers = set("0123456789")
        nums_only = list(filter(lambda x: x in numbers, string))
        return int(nums_only[0] + nums_only[-1])

    result = sum(get_calibration_value(string) for string in input)
    print(f"Part 1: {result}")


def part2(input: list[str]) -> None:
    def get_calibration_value(string: str) -> int:
        mappings = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

        numbers = set("0123456789")
        value = 0

        for i in range(len(string)):
            if string[i] in numbers:
                value += int(string[i]) * 10
                break

            finished = False
            for j in range(i + 2, len(string)):
                if string[i:j] in mappings:
                    value += mappings[string[i:j]] * 10
                    finished = True
                    break

            if finished: break

        mappings = {key[::-1]: value for key, value in mappings.items()}
        string = string[::-1]

        for i in range(len(string)):
            if string[i] in numbers:
                value += int(string[i])
                break

            finished = False
            for j in range(i + 2, len(string)):
                if string[i:j] in mappings:
                    value += mappings[string[i:j]]
                    finished = True
                    break

            if finished: break

        return value

    result = sum(get_calibration_value(string) for string in input)
    print(f"Part 2: {result}")


if __name__ == "__main__":
    input = read.get_input(1, 2023)

    part1(input)
    part2(input)
