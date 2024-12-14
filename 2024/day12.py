import read


def part_1(input: list[str]) -> int:
    from collections import deque

    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

    def sum_tuple(t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
        return t1[0] + t2[0], t1[1] + t2[1]

    def flood_fill(x, y, visited_poses) -> int:

        poses = deque([(x, y)])
        directions = [UP, DOWN, LEFT, RIGHT]

        type = input[y][x]

        all_poses = set()
        while poses:
            x, y = pos = poses.pop()
            input[y][x] = "."
            all_poses.add((x, y))
            for direction in directions:
                nx, ny = sum_tuple(pos, direction)
                if nx < 0 or nx >= len(input[0]) or ny < 0 or ny >= len(input):
                    continue
                if input[ny][nx] != type:
                    continue
                poses.append((nx, ny))

        perimeter = 0
        for pos in all_poses:
            for direction in directions:
                nx, ny = sum_tuple(pos, direction)
                if nx < 0 or nx >= len(input[0]) or ny < 0 or ny >= len(input):
                    perimeter += 1
                    continue
                if input[ny][nx] != type:
                    if input[ny][nx] != '.':
                        perimeter += 1
                    continue

        visited_poses |= all_poses
        for pos in all_poses:
            x, y = pos
            input[y][x] = type

        # print(type, perimeter, len(all_poses))
        return perimeter * len(all_poses)


    input = [list(line) for line in input]
    total = 0

    visited_poses = set()
    for i, line in enumerate(input):
        for j, char in enumerate(line):
            if (j, i) not in visited_poses:
                total += flood_fill(j, i, visited_poses)

    return total


def part_2(input: list[str]) -> int:
    from collections import deque

    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

    def sum_tuple(t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
        return t1[0] + t2[0], t1[1] + t2[1]

    def flood_fill(x, y, visited_poses) -> int:

        poses = deque([(x, y)])
        directions = [UP, DOWN, LEFT, RIGHT]

        type = input[y][x]

        all_poses = set()
        # sides = 0
        while poses:
            x, y = pos = poses.pop()
            input[y][x] = "."
            all_poses.add((x, y))
            for direction in directions:
                nx, ny = sum_tuple(pos, direction)
                if nx < 0 or nx >= len(input[0]) or ny < 0 or ny >= len(input):
                    continue
                if input[ny][nx] != type:
                    continue
                poses.append((nx, ny))


        inverse = {LEFT: RIGHT, UP: DOWN, DOWN: UP, RIGHT: LEFT}
        perimeter_positions = {}
        for pos in all_poses:
            for direction in directions:
                nx, ny = sum_tuple(pos, direction)
                if nx < 0 or nx >= len(input[0]) or ny < 0 or ny >= len(input):
                    perimeter_positions[(nx, ny)] = direction
                    continue
                if input[ny][nx] != type:
                    if input[ny][nx] != '.':
                        perimeter_positions[(nx, ny)] = direction
                    continue

        marked_off = set()
        sides = 0
        for pos in perimeter_positions:
            if pos in marked_off: continue
            marked_off.add(pos)

            added1 = False
            for direction in (UP, DOWN):
                new_pos = pos

                while True:
                    nx, ny = new_pos = sum_tuple(new_pos, direction)
                    if new_pos in perimeter_positions:
                        marked_off.add(new_pos)
                        added1 = True
                        continue
                    break
            sides += added1

            added2 = False
            for direction in (LEFT, RIGHT):
                new_pos = pos

                while True:
                    nx, ny = new_pos = sum_tuple(new_pos, direction)
                    if new_pos in perimeter_positions:
                        marked_off.add(new_pos)
                        added2 = True
                        continue
                    break
            sides += added2

            if added1 == added2 == False:
                sides += 1

        visited_poses |= all_poses
        for pos in all_poses:
            x, y = pos
            input[y][x] = type

        print(type, sides, len(all_poses))
        return len(perimeter_positions) * len(all_poses)


    input = [list(line) for line in input]
    total = 0

    visited_poses = set()
    for i, line in enumerate(input):
        for j, char in enumerate(line):
            if (j, i) not in visited_poses:
                total += flood_fill(j, i, visited_poses)

    return total


if __name__ == "__main__":
    input = read.load_from_file("test")
    print(part_2(input))

    # day = 12
    # read.save_input_to_file(day, 2024)
    # read.test_solution(day, 2024, part_1, part_2)
