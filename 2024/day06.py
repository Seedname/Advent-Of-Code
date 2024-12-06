import read
from dataclasses import dataclass


class Direction:
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


@dataclass
class Guard:
    position: tuple[int, int]
    facing: tuple[int, int]


def get_positions(input: list[str]):
    positions = set()

    guard: Guard = Guard((0, 0), Direction.UP)

    direction_mappings = {Direction.UP: Direction.RIGHT,
                          Direction.RIGHT: Direction.DOWN,
                          Direction.DOWN: Direction.LEFT,
                          Direction.LEFT: Direction.UP,
                         }

    for i, line in enumerate(input):
        if "^" in line:
            guard.position = (line.index("^"), i)
            positions.add(guard.position)
            break

    while True:
        next_x, next_y = (guard.position[0] + guard.facing[0], guard.position[1] + guard.facing[1])

        if next_x < 0 or next_y < 0 or next_x >= len(input) or next_y >= len(input[0]):
            break

        if input[next_y][next_x] == "#":
            guard.facing = direction_mappings[guard.facing]
        else:
            guard.position = (next_x, next_y)
            positions.add(guard.position)

    return positions


def part_1(input: list[str]) -> int:
    return len(get_positions(input))


def part_2(input: list[str]) -> int:
    guard: Guard = Guard((0, 0), Direction.UP)

    direction_mappings = {Direction.UP: Direction.RIGHT,
                          Direction.RIGHT: Direction.DOWN,
                          Direction.DOWN: Direction.LEFT,
                          Direction.LEFT: Direction.UP,
                          }

    for i, line in enumerate(input):
        if "^" in line:
            guard.position = (line.index("^"), i)
            break

    default_position = tuple(guard.position)

    def obstruction_causes_loop(x, y, guard, input: list[str]):
        positions = set()
        positions.add((guard.position, guard.facing))

        new_input: list[str] = [line[:] for line in input]
        new_input[y] = new_input[y][:x] + "#" + new_input[y][x+1:]

        while True:
            next_x, next_y = (guard.position[0] + guard.facing[0], guard.position[1] + guard.facing[1])

            if next_x < 0 or next_y < 0 or next_y >= len(new_input) or next_x >= len(new_input[0]):
                return False

            if new_input[next_y][next_x] == "#":
                guard.facing = direction_mappings[guard.facing]
            else:
                guard.position = (next_x, next_y)
                if (guard.position, guard.facing) in positions:
                    return True
                positions.add((guard.position, guard.facing))

    total = 0
    positions = get_positions(input)
    positions.remove(guard.position)
    for position in positions:
        x, y = position
        guard.position = default_position
        guard.facing = Direction.UP
        if obstruction_causes_loop(x, y, guard, input):
            total += 1

    return total


if __name__ == "__main__":
    read.test_solution(6, 2024, part_2)
