import read
from tqdm import tqdm


def part_1(input: list[str]) -> int:
    storage = list(map(int, list(input[0])))
    blocks = []

    for i, amount in enumerate(storage):
        if i % 2 == 0:
            blocks += [i // 2] * amount
        else:
            blocks += ["."] * amount

    def get_next_empty_space():
        for i, item in enumerate(blocks):
            if item == ".":
                return i

    for i in tqdm(range(len(blocks)-1, -1, -1)):
        next_space = get_next_empty_space()
        if next_space > i:
            blocks = blocks[:i+1]
            break
        blocks[next_space] = blocks[i]
        blocks[i] = "."

    checksum = 0
    for i, item in enumerate(blocks):
        checksum += item * i

    return checksum


def part_2(input: list[str]) -> int:
    storage = list(map(int, list(input[0])))
    blocks = []


    files = []
    for i, amount in enumerate(storage):
        if i % 2 == 0:
            files.append((len(blocks), amount))
            blocks += [i // 2] * amount
        else:
            blocks += ["."] * amount

    def get_next_empty_chunk_of_size(n: int):
        i = 0
        while i < len(blocks) - n:
            if blocks[i] != ".":
                i += 1
                continue
            free = all(item == "." for item in blocks[i:i+n])
            if free:
                return i
            i += 1

        return len(blocks)

    for i in tqdm(range(len(files)-1, -1, -1)):
        index, size = files[i]
        item = blocks[index]
        next_space = get_next_empty_chunk_of_size(size)

        if next_space > index:
            continue

        for j in range(size):
            blocks[next_space + j] = item
            blocks[index + j] = "."

    checksum = 0
    for i, item in enumerate(blocks):
        if item == ".": continue
        checksum += item * i

    return checksum


if __name__ == "__main__":
    day = 9
    read.save_input_to_file(day, 2024)
    read.test_solution(day, 2024, part_2)
