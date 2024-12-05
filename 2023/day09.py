import read


def part_1(input: list[str]) -> int:
    def get_next(row: list[int]) -> int:
        rows = [row]
        while not all(item == 0 for item in rows[-1]):
            rows.append([rows[-1][i]-rows[-1][i-1] for i in range(1, len(rows[-1]))])
        rows[-1].append(0)
        for i in range(len(rows)-2, -1, -1):
            rows[i].append(rows[i+1][-1] + rows[i][-1])
        return rows[0][-1]
    return sum(get_next(list(map(int, row.strip().split(" ")))) for row in input)


def part_2(input: list[str]) -> int:
    def get_previous(row: list[int]) -> int:
        rows = [row]
        while not all(item == 0 for item in rows[-1]):
            rows.append([rows[-1][i]-rows[-1][i-1] for i in range(1, len(rows[-1]))])
        rows[-1].insert(0, 0)
        for i in range(len(rows)-2, -1, -1):
            rows[i].insert(0, rows[i][0] - rows[i+1][0])

        return rows[0][0]
    return sum(get_previous(list(map(int, filter(lambda x: x.strip() != "", row.strip().split(" "))))) for row in input)


if __name__ == "__main__":
    read.test_solution(9, 2023, part_1, part_2)