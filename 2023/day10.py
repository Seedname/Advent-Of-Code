# import read
# from collections import deque, defaultdict
# from dataclasses import dataclass, field
#
#
# @dataclass
# class Node:
#     next: tuple[int, int] = None
#
# @dataclass
# class RootNode:
#     next: list[tuple[int, int]] = field(default_factory=lambda: [])
#     distance: int = 0
#     # north: tuple[int, int] = (None, None)
#     # east: tuple[int, int] = (None, None)
#     # south: tuple[int, int] = (None, None)
#     # west: tuple[int, int] = (None, None)
#
#
# def part_1(input: list[str]) -> int:
#     for i, row in enumerate(input):
#         if 'S' in row:
#             starting_pos = (i, row.index('S'))
#             break
#
#     y1, x1 = starting_pos
#     poses = deque([((x1, y1), (x1-1, y1)),
#                    ((x1, y1), (x1+1, y1)),
#                    ((x1, y1), (x1, y1-1)),
#                    ((x1, y1), (x1, y1+1))])
#
#     # graph = {starting_pos: [None] * 4}
#     graph = defaultdict(Node)
#     w, h = len(input[0]), len(input)
#
#     graph[starting_pos] = RootNode()
#
#     while len(poses) > 0:
#         previous_pos, current_pos = poses.pop()
#         px, py = previous_pos
#         cx, cy = current_pos
#         previous_icon, current_icon = input[py][px], input[cy][cx]
#
#         if current_icon == ".":
#             continue
#
#         if current_icon == "S":
#             graph[previous_pos].next = current_pos
#
#             break
#
#         if current_icon == "7":
#             if previous_icon in {"-", "F", "L", "S"} and cx > px: # 7 to the east
#                 if previous_icon == "S":
#                     graph[previous_pos].next.append(current_pos)
#                 else:
#                     graph[previous_pos].next = current_pos
#                 poses.append((current_pos, (cx, cy+1))) # go south past pipe
#             elif previous_icon in {"|", "J", "L", "S"} and cy < py: # 7 to the north
#                 if previous_icon == "S":
#                     graph[previous_pos].next.append(current_pos)
#                 else:
#                     graph[previous_pos].next = current_pos
#                 poses.append((current_pos, (cx-1, cy))) # go west past pipe
#
#             continue
#
#         if current_icon == "F":
#             if previous_icon in {"-", "J", "7", "S"} and cx < px: # F to the west
#                 if previous_icon == "S":
#                     graph[previous_pos].next.append(current_pos)
#                 else:
#                     graph[previous_pos].next = current_pos
#                 poses.append((current_pos, (cx, cy+1))) # go south past pipe
#             elif previous_icon in {"|", "J", "L", "S"} and cy < py: # F to the north
#                 if previous_icon == "S":
#                     graph[previous_pos].next.append(current_pos)
#                 else:
#                     graph[previous_pos].next = current_pos
#                 poses.append((current_pos, (cx+1, cy))) # go east past pipe
#
#             continue
#
#         if current_icon == "L":
#             if previous_icon in {"-", "J", "7", "S"} and cx < px: # L to the west
#                 if previous_icon == "S":
#                     graph[previous_pos].next.append(current_pos)
#                 else:
#                     graph[previous_pos].next = current_pos
#                 poses.append((current_pos, (cx, cy-1))) # go north past pipe
#             elif previous_icon in {"|", "7", "F", "S"} and cy > py: # L to the south
#                 if previous_icon == "S":
#                     graph[previous_pos].next.append(current_pos)
#                 else:
#                     graph[previous_pos].next = current_pos
#                 poses.append((current_pos, (cx+1, cy))) # go east past pipe
#             continue
#
#         if current_icon == "J":
#             if previous_icon in {"-", "L", "F", "S"} and cx > px: # J to the east
#                 if previous_icon == "S":
#                     graph[previous_pos].next.append(current_pos)
#                 else:
#                     graph[previous_pos].next = current_pos
#                 poses.append((current_pos, (cx, cy-1))) # go north past pipe
#             elif previous_icon in {"|", "7", "F", "S"} and cy > py: # J to the south
#                 if previous_icon == "S":
#                     graph[previous_pos].next.append(current_pos)
#                 else:
#                     graph[previous_pos].next = current_pos
#                 poses.append((current_pos, (cx-1, cy))) # go west past pipe
#             continue
#
#         if current_icon == "|":
#             if previous_icon in {"F", "7", "S"} and cy > py: # | to the south
#                 if previous_icon == "S":
#                     graph[previous_pos].next.append(current_pos)
#                 else:
#                     graph[previous_pos].next = current_pos
#                 poses.append((current_pos, (cx, cy+1))) # keep going south
#             elif previous_icon in {"J", "L", "S"} and cy < py: # | to the south
#                 if previous_icon == "S":
#                     graph[previous_pos].next.append(current_pos)
#                 else:
#                     graph[previous_pos].next = current_pos
#                 poses.append((current_pos, (cx, cy-1))) # keep going north
#             continue
#
#         if current_icon == "-":
#             if previous_icon in {"F", "L", "S"} and cx > px: # - to the east
#                 if previous_icon == "S":
#                     graph[previous_pos].next.append(current_pos)
#                 else:
#                     graph[previous_pos].next = current_pos
#                 poses.append((current_pos, (cx+1, cy))) # keep going east
#             elif previous_icon in {"J", "L", "S"} and cx < px: # | to the west
#                 if previous_icon == "S":
#                     graph[previous_pos].next.append(current_pos)
#                 else:
#                     graph[previous_pos].next = current_pos
#                 poses.append((current_pos, (cx-1, cy))) # keep going west
#             continue
#
#     current_pos = starting_pos
#
#     steps = 0
#
#     pos = graph[current_pos].next[1]
#     while True:
#         steps += 1
#         current_node = graph[pos]
#         if current_node.next is None: break
#         pos = current_node.next
#         if input[pos[1]][pos[0]] == "S": break
#
#
#     print(steps)
#
#
# def part_2(input: list[str]) -> int:
#     pass
#
#
# if __name__ == "__main__":
#     read.test_solution(10, 2023, None, None, part_1, part_2)

import read
from collections import deque


def part_1(input: list[str]) -> int:
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)


    connections = {"|": {UP: UP,
                         DOWN: DOWN},
                   "-": {LEFT: LEFT,
                         RIGHT: RIGHT},
                   "7": {RIGHT: DOWN,
                         UP: LEFT},
                   "L": {DOWN: RIGHT,
                         LEFT: UP},
                   "F": {UP: RIGHT,
                         LEFT: DOWN},
                   "J": {RIGHT: UP,
                         DOWN: LEFT}
                   }


    for i, line in enumerate(input):
        if "S" in line:
            starting_position = (line.index("S"), i)

    x1, y1 = starting_position
    poses = deque([((x1, y1), UP),
                   ((x1, y1), DOWN),
                   ((x1, y1), LEFT),
                   ((x1, y1), RIGHT)])

    valid_poses = set()

    while poses:
        prev_pos, direction = poses.pop()
        px, py = prev_pos
        cx, cy = curr_pos = (px + direction[0], py + direction[1])
        prev_icon, curr_icon = input[py][px], input[cy][cx]

        if curr_icon == ".": continue
        if curr_icon == "S": continue

        if direction not in connections[curr_icon]: continue

        valid_poses.add(curr_pos)
        poses.append((curr_pos, connections[curr_icon][direction]))

    return len(valid_poses) // 2 + 1


def part_2(input: list[str]) -> int:
    # if len(input) > 100: return
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)


    connections = {"|": {UP: UP,
                         DOWN: DOWN},
                   "-": {LEFT: LEFT,
                         RIGHT: RIGHT},
                   "7": {RIGHT: DOWN,
                         UP: LEFT},
                   "L": {DOWN: RIGHT,
                         LEFT: UP},
                   "F": {UP: RIGHT,
                         LEFT: DOWN},
                   "J": {RIGHT: UP,
                         DOWN: LEFT}
                   }


    for i, line in enumerate(input):
        if "S" in line:
            starting_position = (line.index("S"), i)

    x1, y1 = starting_position
    poses = deque([((x1, y1), UP),
                   ((x1, y1), DOWN),
                   ((x1, y1), LEFT),
                   ((x1, y1), RIGHT)])

    valid_poses = set()

    while poses:
        prev_pos, direction = poses.pop()
        px, py = prev_pos
        cx, cy = curr_pos = (px + direction[0], py + direction[1])
        prev_icon, curr_icon = input[py][px], input[cy][cx]

        if curr_icon == ".": continue
        if curr_icon == "S": continue

        if direction not in connections[curr_icon]: continue

        valid_poses.add(curr_pos)
        poses.append((curr_pos, connections[curr_icon][direction]))

    input = [list(line) for line in input]
    for pos in valid_poses:
        x, y = pos
        input[y][x] = "X"

    input[y1][x1] = "X"


    def sum_tuple(t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
        return t1[0] + t2[0], t1[1] + t2[1]

    def flood_fill(x, y) -> None:
        poses = deque([(x, y)])
        directions = [UP, DOWN, LEFT, RIGHT]

        surrounded = True
        all_poses = [(x, y)]
        while poses:
            x, y = pos = poses.pop()
            input[y][x] = "Y"
            for direction in directions:
                nx, ny = sum_tuple(pos, direction)
                if nx < 0 or nx >= len(input[0]) or ny < 0 or ny >= len(input):
                    surrounded = False
                    continue
                if input[ny][nx] in {"X", "Y", "I", "O"}: continue
                poses.append((nx, ny))
                all_poses.append((nx, ny))

        if surrounded:
            for pos in all_poses:
                x, y = pos
                input[y][x] = "I"
        else:
            for pos in all_poses:
                x, y = pos
                input[y][x] = "O"

    for i, line in enumerate(input):
        for j, char in enumerate(line):
            if char not in {"X", "Y", "I", "O"}:
                flood_fill(j, i)

    with open('output', 'w') as f:
        f.write("\n".join(''.join(line) for line in input))

    return sum(line.count("I") for line in input)


if __name__ == "__main__":
    input = read.load_from_file("test")
    print(part_2(input))
    # read.save_input_to_file(10, 2023)
    # read.test_solution(10, 2023, *[None] * 12, part_2)