import read
import re
from tqdm import tqdm

# from sympy.solvers.diophantine import diophantine, diop_solve
# from sympy import solve, solve_univariate_inequality, S, symbols
#
# import math


def part_1(input: list[str]) -> int:
    input = [line for line in input if line.strip() != ""]

    total = 0
    for i in tqdm(range(0, len(input), 3)):
        x1, y1 = tuple(map(int, re.findall('X\+(\d+), Y\+(\d+)', input[i])[0]))
        x2, y2 = tuple(map(int, re.findall('X\+(\d+), Y\+(\d+)', input[i+1])[0]))
        x_prize, y_prize = tuple(map(int, re.findall('X=(\d+), Y=(\d+)', input[i+2])[0]))


        for a in range(1000):
            for b in range(1000):
                if x1 * a + x2 * b == x_prize and y1 * a + y2 * b == y_prize:
                    total += 3 * a + b
                    break
            else:
                continue
            break
        else:
            continue
    return total


import numpy as np
import math

def part_2(input: list[str]) -> int:
    input = [line for line in input if line.strip() != ""]

    total = 0
    def is_int(tup: tuple[float, float]) -> bool | tuple[int, int]:
        a, b = tup
        threshold = 0.001
        if abs(round(a) - a) > threshold: return False
        if abs(round(b) - b) > threshold: return False
        return round(a), round(b)

    for i in tqdm(range(0, len(input), 3)):
        x1, y1 = tuple(map(int, re.search('X\+(\d+), Y\+(\d+)', input[i]).groups()))
        x2, y2 = tuple(map(int, re.search('X\+(\d+), Y\+(\d+)', input[i+1]).groups()))
        x_prize, y_prize = tuple(map(int, re.search('X=(\d+), Y=(\d+)', input[i+2]).groups()))

        # x1 * a + x2 * b = x_prize - x2 * b
        # y1 * a + y2 * b = y_prize
        x_prize += 10000000000000
        y_prize += 10000000000000
        b = (y_prize - y1 * x_prize / x1) / (-y1 * x2 / x1 + y2)
        a = (x_prize - x2 * b) / x1
        result = is_int((a, b))
        if result is False: continue
        a, b = result
        total += 3 * a + b
        # print(a, b)
        # result = is_int((a, b))
        # if result is False: continue
        # a, b = result
        # total += 3 * a + b

    return total

    # total = 0
    # a, b = symbols("a, b", integer=True)

    # for i in tqdm(range(0, len(input), 3)):
    #     x1, y1 = tuple(map(int, re.findall('X\+(\d+), Y\+(\d+)', input[i])[0]))
    #     x2, y2 = tuple(map(int, re.findall('X\+(\d+), Y\+(\d+)', input[i+1])[0]))
    #
    #     x_prize, y_prize = tuple(map(int, re.findall('X=(\d+), Y=(\d+)', input[i+2])[0]))
    #     # print(x_prize / (x1 + x2))
    #     # x_prize += 1_000_000
    #     # y_prize += 1_000_000
    #
    #     # x1 * a + x2 * b == x_prize
    #     # y1 * a + y2 * b == y_prize
    #
    #     # result = diophantine.solve([[x1, y1], [x2, y2]], [x_prize, y_prize])
    #     # print(result)
    #     result = diop_solve(x1 * a + x2 * b + y1 * a + y2 * b - x_prize - y_prize)
    #     x, y = result
    #     x_ = x
    #     y_ = y
    #
    #     if len(result) == 0: continue
    #
    #     t_0 = symbols("t_0", integer=True)
    #
    #     result = solve([x >= 0, y >= 0])
    #     x = result.args[0]
    #     y = result.args[1]
    #
    #
    #     x = solve_univariate_inequality(x, t_0, domain=S.Integers).args[1]
    #     y = solve_univariate_inequality(y, t_0, domain=S.Integers).args[1]
    #
    #     min_value = 1e10000
    #     min_solution = ()
    #
    #     for i in range(x, y + 1):
    #         e = x_.subs(t_0, i)
    #         f = y_.subs(t_0, i)
    #         if 3 * e + f < min_value:
    #             min_value = 3 * e + f
    #             min_solution = (e, f)
    #
    #     g, h = min_solution
    #     print(x1 * g + x2 * h, x_prize)
    #     print(y1 * g + y2 * h, y_prize)

    return total



if __name__ == "__main__":
    input = read.load_from_file("test")
    print(part_2(input))
    # day = 13
    # read.save_input_to_file(day, 2024)
    # read.test_solution(day, 2024, part_1, part_2)
