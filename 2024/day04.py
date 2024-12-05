import read


def part_1(input: list[str]) -> int:
    total = 0
    # if len(input) > 100: return 0

    rows = len(input)
    cols = len(input[0])

    #horizontal
    for row in input:
        total += row.count("XMAS")
        total += row.count("SAMX")

    # vertical
    for i in range(len(input[0])):
        col = ''.join([input[j][i] for j in range(len(input))])
        total += col.count("XMAS")
        total += col.count("SAMX")

    for d in range(rows + cols - 1):
        diagonal = []
        for row in range(rows):
            col = d - row
            if 0 <= col < cols:
                diagonal.append(input[row][col])
        if len(diagonal) >= 4:
            diag = ''.join(diagonal)
            total += diag.count("XMAS")
            total += diag.count("SAMX")

    for d in range(rows + cols - 1):
        diagonal = []
        for row in range(rows):
            col = row - d + cols - 1
            if 0 <= col < cols:
                diagonal.append(input[row][col])
        if len(diagonal) >= 4:
            diag = ''.join(diagonal)
            total += diag.count("XMAS")
            total += diag.count("SAMX")


    return total


def part_2(input: list[str]) -> int:
    total = 0
    for i in range(len(input)-2):
        for j in range(len(input)-2):
            diag1 = ''
            diag2 = ''
            for k in range(3):
                diag1 += input[i+k][j+k]
                diag2 += input[i+2-k][j+k]

            if (diag1 == diag2 or diag1 == diag2[::-1]) and (diag1 == "MAS" or diag1 == "SAM"):
                total += 1

    return total



if __name__ == "__main__":
    read.test_solution(4, 2024, None, None, part_1, None, part_2)
