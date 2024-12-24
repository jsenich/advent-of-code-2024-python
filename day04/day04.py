import re


def extract_grid(puzzle_input: str) -> list[list[str]]:
    grid = []
    for line in puzzle_input.splitlines():
        grid.append(list(line))

    return grid

def grid_to_str(grid: list[list[str]]) -> str:
    output = ""
    for line in grid:
        output += f"{''.join(line)}\n"
    
    return output

def rotate_grid(grid: list[list[str]]) -> list[list[str]]:
    return list(zip(*grid[::-1]))

def count_xmas(grid: list[list[str]]) -> int:
    xmas_count: int = 0

    grid_str = grid_to_str(grid)

    xmas_count += len(re.findall("XMAS", grid_str))
    xmas_count += len(re.findall("SAMX", grid_str))

    return xmas_count

def read_diagonals(grid):
    """Reads all diagonals of a 2D grid (list of lists)."""

    diagonals = []

    # Top-left to bottom-right diagonals
    for i in range(len(grid)):
        diagonal = []
        for j in range(min(len(grid) - i, len(grid[i]))):
            diagonal.append(grid[i + j][j])
        diagonals.append(diagonal)

    for i in range(1, len(grid[0])):
        diagonal = []
        for j in range(min(len(grid), len(grid[0]) - i)):
            diagonal.append(grid[j][i + j])
        diagonals.append(diagonal)

    # Top-right to bottom-left diagonals
    for i in range(len(grid)):
        diagonal = []
        for j in range(min(len(grid) - i, len(grid[i]))):
            diagonal.append(grid[i + j][len(grid[i]) - 1 - j])
        diagonals.append(diagonal)

    for i in range(1, len(grid[0]) - 1):
        diagonal = []
        for j in range(min(len(grid), len(grid[0]) - i)):
            diagonal.append(grid[j][len(grid[0]) - 1 - i - j])
        diagonals.append(diagonal)

    return diagonals


def part_one(puzzle_input: str) -> int:
    xmas_count: int = 0

    grid = extract_grid(puzzle_input)
    xmas_count += count_xmas(grid)
    xmas_count += count_xmas(rotate_grid(grid))
    xmas_count += count_xmas(read_diagonals(grid))

    return xmas_count

def part_two(puzzle_input: str) -> int:
    pass

if __name__ == "__main__":
    with open('day04/input.txt') as f:
        puzzle_input = f.read().strip()

    print(f"part one: {part_one(puzzle_input)}")
    # print(f"part two: {part_two(puzzle_input)}")