import pytest
from day03.day03 import part_one, part_two

sample_puzzle_partone = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
sample_puzzle_parttwo = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open('day03/input.txt') as f:
    live_puzzle_input = f.read().strip()
 

@pytest.mark.parametrize("puzzle_input,expected", [(sample_puzzle_partone, 161), (live_puzzle_input, 189600467)])
def test_part_one(puzzle_input, expected):

    actual = part_one(puzzle_input)

    assert actual == expected

@pytest.mark.parametrize("puzzle_input,expected", [(sample_puzzle_parttwo, 48), (live_puzzle_input, 107069718)])
def test_part_two(puzzle_input, expected):

    actual = part_two(puzzle_input)

    assert actual == expected