import read


def part1(input: list[str]) -> None:
    _, times = input[0].split(":")
    times = map(int, filter(lambda x: x != "", map(str.strip, times.split(" "))))
    _, distances = input[1].split(":")
    distances = map(int, filter(lambda x: x != "", map(str.strip, distances.split(" "))))

    times_distance = zip(times, distances)
    prod = 1
    for time, distance in times_distance:
        ways = 0
        for i in range(time+1):
            d = (time - i) * i
            if d > distance:
                ways += 1
        prod *= ways

    print(f"Part 1: {prod}")


def part2(input: list[str]) -> None:
    _, times = input[0].split(":")
    time = int(''.join(filter(lambda x: x != "", map(str.strip, times.split(" ")))))
    _, distances = input[1].split(":")
    distance = int(''.join(filter(lambda x: x != "", map(str.strip, distances.split(" ")))))
    ways = 0
    for i in range(time+1):
        d = (time - i) * i
        if d > distance:
            ways += 1

    print(f"Part 2: {ways}")


if __name__ == "__main__":
    input = read.load_input(6, 2023)
    # input = read.load_from_file("four")
    part1(input)
    part2(input)