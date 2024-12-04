def part_one(puzzle_input: list[str]) -> int:
    safe_reports = 0

    for report in puzzle_input:
        levels = [int(l) for l in report.split(" ")]
        increasing = False
        safe = False
        if levels[1] > levels[0]:
            increasing = True
        elif levels[1] == levels[0]:
            continue
        for i, level in enumerate(levels):
            if i < len(levels) - 1:
                if increasing:
                    if levels[i + 1] > levels[i] and levels[i + 1] - levels[i] <= 3:
                        safe = True
                    else:
                        safe = False
                        break
                else:
                    if levels[i + 1] < levels[i] and levels[i] - levels[i + 1] <= 3:
                        safe = True
                    else:
                        safe = False
                        break

        if safe:
            safe_reports += 1
    return safe_reports

def is_safe(levels: list[int]) -> bool:
    increasing = False
    if levels[1] > levels[0]:
        increasing = True

    for i, level in enumerate(levels):
        if i < len(levels) - 1:
            if increasing:
                if levels[i + 1] > levels[i] and (levels[i + 1] - levels[i]) <= 3:
                    pass
                else:
                    return False
            else:
                if levels[i + 1] < levels[i] and 1 <= (levels[i] - levels[i + 1]) <= 3:
                    pass
                else:
                    return False

    return True


def part_two(puzzle_input: list[str]) -> int:
    safe_reports = 0
    for report in puzzle_input:
        levels = [int(l) for l in report.split(" ")]

        if is_safe(levels):
            safe_reports += 1
        else:
            unsafe_count: int = 1
            for i in range(len(levels)):
                dampened_levels = levels[:i] + levels[i + 1:]
                if is_safe(dampened_levels):
                    safe_reports += 1
                    break

    return safe_reports

if __name__ == "__main__":
    with open('day02/input.txt') as f:
        puzzle_input = f.read().strip().splitlines()

    print(f"part one: {part_one(puzzle_input)}")
    print(f"part two: {part_two(puzzle_input)}") # not 540