from collections import Counter

def part_one(puzzle_input: list[str]) -> int:
    left = []
    right = []
    for line in puzzle_input:
        l, r = line.split("   ")
        left.append(int(l))
        right.append(int(r))

    left.sort()
    right.sort()

    total = sum(abs(l - r) for l, r in zip(left, right))

    return total

def part_two(puzzle_input: list[str]) -> int:
    left = []
    right = []
    for line in puzzle_input:
        l, r = line.split("   ")
        left.append(l)
        right.append(r)
    
    right_dict = Counter(right)

    total = sum(int(n) * right_dict[n] for n in left)

    return total

if __name__ == "__main__":
    with open('day01/input.txt') as f:
        puzzle_input = f.read().strip().splitlines()

    print(f"part one: {part_one(puzzle_input)}")
    print(f"part two: {part_two(puzzle_input)}")

# part one answer: 2375403
# part two answer: 23082277