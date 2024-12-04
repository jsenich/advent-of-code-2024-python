import pytest
from day03.day03 import part_one

sample_puzzle_input = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

with open('day03/input.txt') as f:
    live_puzzle_input = f.read().strip()
 

@pytest.mark.parametrize("puzzle_input,expected", [(sample_puzzle_input, 161), (live_puzzle_input, 189600467)])
def test_part_one(puzzle_input, expected):

    actual = part_one(puzzle_input)

    assert actual == expected
