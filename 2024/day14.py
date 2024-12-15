from collections import defaultdict, Counter

import read
from dataclasses import dataclass
import re
from tqdm import tqdm
import sys

sys.setrecursionlimit(10**6)

@dataclass
class Robot:
    x: int
    y: int
    vx: int
    vy: int


def part_1(input: list[str]) -> int:
    width = 101
    height = 103
    robots = [Robot(*map(int, re.findall('p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line.strip())[0])) for line in input]

    def get_robot_position(robot, n):
        if n == 0:
            return robot.x, robot.y

        nx = (robot.x + robot.vx) % width

        if nx < 0:
            nx += width

        ny = (robot.y + robot.vy) % height

        if ny < 0:
            nx += height

        return get_robot_position(Robot(nx, ny, robot.vx, robot.vy), n-1)

    quadrants = defaultdict(int)
    # poses = defaultdict(int)
    for robot in robots:
        rx, ry = get_robot_position(robot, 100)
        # poses[(rx, ry)] += 1
        if rx == width // 2: continue
        if ry == height // 2: continue

        if rx < width / 2 and ry < height / 2:
            quadrants[0] += 1
        elif rx > width / 2 and ry < height / 2:
            quadrants[1] += 1
        elif rx > width / 2 and ry > height / 2:
            quadrants[2] += 1
        elif rx < width / 2 and ry > height / 2:
            quadrants[3] += 1


    # with open('output', 'w') as f:
    #     grid = [['.' for _ in range(width)] for _ in range(height)]
    #     for pos in poses:
    #         grid[pos[1]][pos[0]] = str(poses[pos])
    #     f.write('\n'.join(''.join(line) for line in grid))

    print(quadrants)
    prod = 1
    for quadrant in quadrants:
        prod *= quadrants[quadrant]

    return prod


def part_2(input: list[str]) -> int:
    width = 101
    height = 103
    robots = [tuple(map(int, re.search('p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line.strip()).groups())) for line in input]

    def get_robot_positions(robots, n):
        for j, robot in enumerate(robots):
            x, y, vx, vy = robot
            nx = (x + vx * n) % width

            while nx < 0:
                nx += width

            ny = (y + vy * n) % height

            while ny < 0:
                nx += height

            robots[j] = (nx, ny, vx, vy)

        poses = [(robot[0], robot[1]) for robot in robots]
        positions = Counter(poses)

        if len(poses) == len(positions):
            print(n)

        return positions

    with open('output', 'w') as f:
        for i in tqdm(range(1, 10000)):
            grid = [['.' for _ in range(width)] for _ in range(height)]
            # positions = Counter(get_robot_position(robot, i) for robot in robots)
            positions = get_robot_positions(robots[:], i)
            for pos in positions:
                grid[pos[1]][pos[0]] = str(positions[pos])
            f.write('\n'.join(''.join(line) for line in grid) + f"\n{i}:\n")

    return -1


if __name__ == "__main__":
    input = read.load_from_file("input14_2024")
    print(part_2(input))
    # day = 14
    # read.save_input_to_file(day, 2024)
    # read.test_solution(day, 2024, part_1, part_2)