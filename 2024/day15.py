import read
import re
from dataclasses import dataclass
from collections import deque

from tqdm import tqdm

def part_1(input: list[str]) -> int:
    walls = set()
    boxes = set()
    robot = ()

    end = 0
    for i, line in enumerate(input):
        if line.strip() == "":
            end = i
            break
        for j, item in enumerate(line):
            if item == "#":
                walls.add((j, i))
            elif item == "O":
                boxes.add((j, i))
            elif item == "@":
                robot = (j, i)

    maps = {"^": (0, -1),
            ">": (1, 0),
            "<": (-1, 0),
            "v": (0, 1)}

    print(input[end:])
    directions = [maps[item] for item in ''.join(input[end:])]

    def sum_tuple(t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
        return t1[0] + t2[0], t1[1] + t2[1]

    for direction in directions:
        x, y = robot
        nx, ny = npos = sum_tuple(robot, direction)
        new_boxes = boxes.copy()

        if npos in walls: continue

        if npos in boxes:
            box = npos
            can_move = True

            new_boxes.discard(box)

            while True:
                next_area = sum_tuple(box, direction)

                if next_area in walls:
                    can_move = False
                    break

                if next_area in boxes:
                    box = next_area
                    continue

                break

            if can_move:
                new_boxes.add(sum_tuple(box, direction))
                boxes = new_boxes
            else: continue

        robot = npos

    with open('output', 'w') as f:
        grid = [['.' for _ in range(len(input[0]))] for _ in range(len(input))]
        for item in walls:
            grid[item[1]][item[0]] = "#"
        for item in boxes:
            grid[item[1]][item[0]] = "O"
        grid[robot[1]][robot[0]] = "@"
        f.write('\n'.join(''.join(line) for line in grid))

    return sum(100 * box[1] + box[0] for box in boxes)


@dataclass
class Box:
    left: tuple[int, int]
    right: tuple[int, int]

    def __hash__(self):
        return hash((self.left, self.right))


def part_2(input: list[str]) -> int:
    walls = set()
    boxes = {}
    robot = ()

    for i, line in enumerate(input):
        if line.strip() == "":
            break
        input[i] = line.replace("#", "##").replace(".", "..").replace("O", "[]").replace("@", "@.")

    width = len(input[0].strip())

    end = 0
    for i, line in enumerate(input):
        if line.strip() == "":
            end = i
            break
        for j, item in enumerate(line):
            if item == "#":
                walls.add((j, i))
            elif item == "[":
                box = Box((j, i), (j+1, i))
                boxes[(j, i)] = box
                boxes[(j+1, i)] = box
            elif item == "@":
                robot = (j, i)

    print(len(set(boxes.values())))

    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    maps = {"^": UP,
            ">": RIGHT,
            "<": LEFT,
            "v": DOWN}

    directions = [maps[item] for item in ''.join(input[end:]).strip()]

    def sum_tuple(t1: tuple[int, int], t2: tuple[int, int]) -> tuple[int, int]:
        return t1[0] + t2[0], t1[1] + t2[1]


    def move_box(box: Box, direction: tuple[int, int]) -> Box:
        return Box(sum_tuple(box.left, direction), sum_tuple(box.right, direction))

    def box_has_collision(box: Box, index: int, boxes: list[Box]) -> Box | bool:
        for i, other in enumerate(boxes):
            if box == other: continue
            if

    for direction in tqdm(directions):
        x, y = robot
        nx, ny = npos = sum_tuple(robot, direction)
        new_boxes = boxes.copy()

        if npos in walls: continue

        if npos in boxes:
            box = move_box(boxes[npos], direction)
            can_move = True

            shift_boxes = deque([box])
            all_boxes = []
            while shift_boxes:
                next_box = shift_boxes.popleft()

                new_boxes.pop(next_box.left, 0)
                new_boxes.pop(next_box.right, 0)

                next_area = move_box(next_box, direction)

                if next_area.left in walls or next_area.right in walls:
                    can_move = False
                    break

                all_boxes.append(next_area)

                if next_area.left in boxes or next_area.right in boxes:
                    left = boxes.get(next_area.left, False)
                    right = boxes.get(next_area.right, False)

                    # if direction == UP or direction == DOWN:
                    #     if left:
                    #         shift_boxes.append(left)
                    #     if right:
                    #         shift_boxes.append(right)
                    #
                    # # if direction == RIGHT:
                    # #     if right:
                    # #         shift_boxes.append(right)
                    # #
                    # # if direction == LEFT:
                    # #     if left:
                    # #         shift_boxes.append(left)

                # print(len(shift_boxes))

            if can_move:
                for box in all_boxes:
                    new_boxes[box.left] = box
                    new_boxes[box.right] = box
                boxes = new_boxes
            else:
                continue

        robot = npos



        # if npos in boxes:
        #     box = npos
        #     can_move = True
        #
        #     new_boxes.discard(box)
        #
        #     while True:
        #         next_area = sum_tuple(box, direction)
        #
        #         if next_area in walls:
        #             can_move = False
        #             break
        #
        #         if next_area in boxes:
        #             box = next_area
        #             continue
        #
        #         break
        #
        #     if can_move:
        #         new_boxes.add(sum_tuple(box, direction))
        #         boxes = new_boxes
        #     else: continue

    with open('output', 'w') as f:
        grid = [['.' for _ in range(len(input[0]))] for _ in range(len(input))]
        for item in walls:
            grid[item[1]][item[0]] = "#"
        for item in boxes.values():
            grid[item.left[1]][item.left[0]] = "["
            grid[item.right[1]][item.right[0]] = "]"

        grid[robot[1]][robot[0]] = "@"
        f.write('\n'.join(''.join(line) for line in grid))

    print(len(set(boxes.values())))
    return sum(100 * box.left[1] + box.left[0] for box in set(boxes.values()))


if __name__ == "__main__":
    input = read.load_from_file("test")
    print(part_2(input))
    # day = 15
    # read.save_input_to_file(day, 2024)
    # read.test_solution(day, 2024, part_1, part_2)
