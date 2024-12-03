import read
from dataclasses import dataclass
from itertools import cycle
import math
#not my best work

@dataclass
class Node:
    name: str
    left: str
    right: str


def part_1(input: list[str]) -> int:
    pattern = input[0]

    nodes = []
    locations = {}
    for i in range(2, len(input)):
        name, end = input[i].split(" = ")
        left, right = end.split(",")
        nodes.append(Node(name, left[1:].strip(), right[:-1].strip()))
        locations[name.strip()] = i - 2

    current_node = nodes[locations['AAA']]

    steps = 0
    while True:
        for step in pattern:
            if step == "L":
                current_node = nodes[locations[current_node.left]]
            else:
                current_node = nodes[locations[current_node.right]]
            steps += 1
            if current_node.name == "ZZZ":
                break
        else:
            continue
        break

    return steps


def part_2(input: list[str]) -> int:
    pattern = input[0]

    nodes = []
    locations = {}
    for i in range(2, len(input)):
        name, end = input[i].split(" = ")
        left, right = end.split(",")
        nodes.append(Node(name, left[1:].strip(), right[:-1].strip()))
        locations[name.strip()] = i - 2

    starting_nodes = [node for node in nodes if node.name[-1] == "A"]

    cycles = []
    for node in starting_nodes:
        steps = 0
        while True:
            for step in pattern:
                if step == "L":
                    node = nodes[locations[node.left]]
                else:
                    node = nodes[locations[node.right]]

                steps += 1

                if node.name[-1] == 'Z':
                    cycles.append(steps)
                    break
            else: continue
            break

        return math.lcm(*cycles)


if __name__ == "__main__":
    read.test_solution(8, 2023, part_1, None, part_2)
