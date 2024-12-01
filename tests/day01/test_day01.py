import pytest
from day01.day01 import part_one, part_two

sample_puzzle_input = """3   4
4   3
2   5
1   3
3   9
3   3
""".strip().splitlines()

with open('day01/input.txt') as f:
    live_puzzle_input = f.read().strip().splitlines()
 

@pytest.mark.parametrize("puzzle_input,expected", [(sample_puzzle_input, 11), (live_puzzle_input, 2375403)])
def test_part_one(puzzle_input, expected):

    actual = part_one(puzzle_input)

    assert actual == expected

@pytest.mark.parametrize("puzzle_input,expected", [(sample_puzzle_input, 31), (live_puzzle_input, 23082277)])
def test_part_two(puzzle_input, expected):

    actual = part_two(puzzle_input)

    assert actual == expected