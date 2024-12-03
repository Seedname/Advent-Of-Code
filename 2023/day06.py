import read


def part_1(input: list[str]) -> int:
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

    return ways


def part_2(input: list[str]) -> int:
    _, times = input[0].split(":")
    time = int(''.join(filter(lambda x: x != "", map(str.strip, times.split(" ")))))
    _, distances = input[1].split(":")
    distance = int(''.join(filter(lambda x: x != "", map(str.strip, distances.split(" ")))))
    ways = 0

    for i in range(time+1):
        d = (time - i) * i
        if d > distance:
            ways += 1

    return ways


if __name__ == "__main__":
    read.test_solution(6, 2023, part_1, part_2)