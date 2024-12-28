import itertools

def part_one(puzzle_input: str) -> int:
    diskmap: list[int] = [int(n) for n in list(puzzle_input.strip())]
    blocks: list[int|None] = []

    file_id = 0
    for i in range(0, len(diskmap), 2):
        file_length = diskmap[i]
        free_space = diskmap[i+1] if i + 1 < len(diskmap) else 0
        blocks.extend([file_id] * file_length)
        if free_space > 0:
            blocks.extend([None] * free_space)
        file_id += 1

    checksum = 0
    for i, n in enumerate(blocks):
        if n is None:
            n = blocks.pop()
            while n is None:
                if len(blocks) <= i:
                    n = 0
                    break
                n = blocks.pop()

        checksum += i * n

    return checksum


if __name__ == "__main__":
    # puzzle_input = """2333133121414131402"""

    with open('day09/input.txt') as f:
        puzzle_input = f.read().strip()


    print(f"part one: {part_one(puzzle_input)}") # Answer: 6288599492129
