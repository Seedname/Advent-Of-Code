import read


def part_1(input: list[str]) -> int:
    from collections import deque

    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

    directions = [UP, RIGHT, DOWN, LEFT]

    input = [list(map(int, list(line))) for line in input]
    zero_positions = set()

    for i, line in enumerate(input):
        for j, item in enumerate(line):
            if item == 0:
                zero_positions.add((j, i))

    total = 0
    for starting_position in zero_positions:
        x1, y1 = starting_position
        poses = deque([((x1, y1), UP),
                       ((x1, y1), DOWN),
                       ((x1, y1), LEFT),
                       ((x1, y1), RIGHT)])

        nine_poses = set()
        while poses:
            prev_pos, direction = poses.pop()
            px, py = prev_pos
            cx, cy = curr_pos = (px + direction[0], py + direction[1])

            if cx < 0 or cx >= len(input[0]) or cy < 0 or cy >= len(input): continue

            prev_item, curr_item = input[py][px], input[cy][cx]

            if curr_item < prev_item: continue
            if curr_item != prev_item + 1: continue
            if curr_item == 9:
                nine_poses.add(curr_pos)
                continue

            for cardinal in directions:
                new_pos = (cx + cardinal[0], cy + cardinal[1])
                if new_pos == prev_pos: continue
                poses.append((curr_pos, cardinal))

        total += len(nine_poses)

    return total


def part_2(input: list[str]) -> int:
    from collections import deque, defaultdict

    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

    directions = [UP, RIGHT, DOWN, LEFT]

    input = [list(map(int, list(line))) for line in input]
    zero_positions = set()

    for i, line in enumerate(input):
        for j, item in enumerate(line):
            if item == 0:
                zero_positions.add((j, i))

    total = 0
    for starting_position in zero_positions:
        x1, y1 = starting_position
        poses = deque([((x1, y1), UP, []),
                       ((x1, y1), DOWN, []),
                       ((x1, y1), LEFT, []),
                       ((x1, y1), RIGHT, [])])

        nine_poses = defaultdict(set)
        while poses:
            prev_pos, direction, previous_items = poses.pop()
            px, py = prev_pos
            cx, cy = curr_pos = (px + direction[0], py + direction[1])

            if cx < 0 or cx >= len(input[0]) or cy < 0 or cy >= len(input): continue

            prev_item, curr_item = input[py][px], input[cy][cx]

            if curr_item < prev_item: continue
            if curr_item != prev_item + 1: continue
            if curr_item == 9:
                nine_poses[curr_pos].add(str(previous_items))
                continue

            for cardinal in directions:
                new_pos = (cx + cardinal[0], cy + cardinal[1])
                if new_pos == prev_pos: continue
                prev_items = previous_items[:]
                prev_items.append(curr_pos)
                poses.append((curr_pos, cardinal, prev_items))

        total += sum(len(path) for path in nine_poses.values())

    return total


if __name__ == "__main__":
    day = 10
    read.save_input_to_file(day, 2024)
    read.test_solution(day, 2024, *[None] * 4, part_2)
