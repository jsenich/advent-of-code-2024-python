import pytest
from day02.day02 import part_one, part_two

sample_puzzle_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip().splitlines()

with open('day02/input.txt') as f:
    live_puzzle_input = f.read().strip().splitlines()
 

@pytest.mark.parametrize("puzzle_input,expected", [(sample_puzzle_input, 2), (live_puzzle_input, 526)])
def test_part_one(puzzle_input, expected):

    actual = part_one(puzzle_input)

    assert actual == expected

@pytest.mark.parametrize("puzzle_input,expected", [(sample_puzzle_input, 4), (live_puzzle_input, 566)])
def test_part_two(puzzle_input, expected):

    actual = part_two(puzzle_input)

    assert actual == expected