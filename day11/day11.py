from copy import deepcopy

def transform_stones(stones: list[int]) -> list[int]:
    new_stones = []
    for i, stone in enumerate(stones):
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            split_index = int(len(s) / 2)
            new_stones.append(int(s[0:split_index]))
            new_stones.append(int(s[split_index:]))
        else:
            new_stones.append(stone * 2024)
    return new_stones

def part_one(stones: list[int]) -> int:
    current_stones = stones
    for _ in range(25):
        current_stones = transform_stones(current_stones)

    return len(current_stones)

if __name__ == "__main__":
    # puzzle_input = """125 17"""

    with open('day11/input.txt') as f:
        puzzle_input = f.read().strip()

    stones = [int(n) for n in puzzle_input.strip().split()]

    print(f"part one: {part_one(deepcopy(stones))}") # Answer: 204022
