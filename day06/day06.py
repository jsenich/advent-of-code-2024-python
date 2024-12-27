
def part_one(puzzle_input: str) -> int:
    current_direction: str = "U"
    move_count: int = 0
    guard_pos: tuple[int, int]
    obstructions: list[tuple[int, int]] = []
    guard_distinct_postions: set[tuple[int, int]] = set()
    is_offmap = False

    rows = puzzle_input.strip().splitlines()
    numrows = len(rows)
    numcols = len(list(rows[0]))
    for row, line in enumerate(puzzle_input.strip().splitlines()):
        for col, value in enumerate(list(line)):
            if value == "^":
                guard_pos = (row, col)
                guard_distinct_postions.add(guard_pos)
            elif value == "#":
                obstructions.append((row, col))

    def is_obstructed(new_pos: tuple[int, int]) -> bool:
        return new_pos in obstructions

    while (not is_offmap):
        row, col = guard_pos

        if current_direction == "U":
            if row - 1 >= 0:
                new_pos = (row - 1, col)
                if is_obstructed(new_pos):
                    current_direction = "R"
                    continue
                guard_distinct_postions.add(new_pos)
                guard_pos = new_pos
            else:
                is_offmap = True
        elif current_direction == "D":
            if row + 1 < numrows:
                new_pos = (row + 1, col)
                if is_obstructed(new_pos):
                    current_direction = "L"
                    continue
                guard_distinct_postions.add(new_pos)
                guard_pos = new_pos
            else:
                is_offmap = True
        elif current_direction == "L":
            if col - 1 >= 0:
                new_pos = (row, col - 1)
                if is_obstructed(new_pos):
                    current_direction = "U"
                    continue
                guard_distinct_postions.add(new_pos)
                guard_pos = new_pos
            else:
                is_offmap = True
        else: # current_direction == "R"
            if col + 1 < numcols:
                new_pos = (row, col + 1)
                if is_obstructed(new_pos):
                    current_direction = "D"
                    continue
                guard_distinct_postions.add(new_pos)
                guard_pos = new_pos
            else:
                is_offmap = True

    return len(guard_distinct_postions)


if __name__ == "__main__":
    with open('day06/input.txt') as f:
        puzzle_input = f.read().strip()

#     puzzle_input = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
# """

    print(f"part one: {part_one(puzzle_input)}") # Answer: 5080
