import re

def part_one(puzzle_input: str) -> int:
    return sum(int(m[0]) * int(m[1]) for m in re.findall(r"mul\((\d+),(\d+)\)", puzzle_input))

def part_two(puzzle_input: str) -> int:
    enabled: bool = True
    total: int = 0

    for m in re.findall(r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", puzzle_input):
        if m[0] == "don't()":
            enabled = False
            continue
        elif m[0] == "do()":
            enabled = True
        else:
            if not enabled:
                continue
            total += int(m[1]) * int(m[2])
    
    return total

if __name__ == "__main__":
    with open('day03/input.txt') as f:
        puzzle_input = f.read().strip()

    print(f"part one: {part_one(puzzle_input)}")
    print(f"part two: {part_two(puzzle_input)}")