import functools

def part_one(puzzle_input: str) -> int:
    l, r = puzzle_input.split("\n\n")
    rule_lines = l.splitlines()
    page_lines = r.splitlines()

    rules = []
    for line in rule_lines:
        rules.append([int(n) for n in line.split("|")])

    pages = []
    for line in page_lines:
        pages.append([int(n) for n in line.split(",")])

    def key_func(n1, n2):
        if [n1, n2] in rules:
            return -1
        elif n1 == n2:
            return 0
        else:
            return 1

    total = 0
    for page_nums in pages:
        sorted_page_nums = sorted(page_nums, key=functools.cmp_to_key(key_func))
        if page_nums == sorted_page_nums:
            total += page_nums[len(page_nums) // 2]

    return total

def part_two(puzzle_input: str) -> int:
    l, r = puzzle_input.split("\n\n")
    rule_lines = l.splitlines()
    page_lines = r.splitlines()

    rules = []
    for line in rule_lines:
        rules.append([int(n) for n in line.split("|")])

    pages = []
    for line in page_lines:
        pages.append([int(n) for n in line.split(",")])

    def key_func(n1, n2):
        if [n1, n2] in rules:
            return -1
        elif n1 == n2:
            return 0
        else:
            return 1

    total = 0
    for page_nums in pages:
        sorted_page_nums = sorted(page_nums, key=functools.cmp_to_key(key_func))
        if page_nums != sorted_page_nums:
            total += sorted_page_nums[len(sorted_page_nums) // 2]

    return total

if __name__ == "__main__":
    with open('day05/input.txt') as f:
        puzzle_input = f.read().strip()

#     puzzle_input = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47
# """.strip()


    print(f"part one: {part_one(puzzle_input)}") # Answer: 4689
    print(f"part two: {part_two(puzzle_input)}") # Answer: 6336
