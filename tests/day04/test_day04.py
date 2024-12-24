import pytest
from day04.day04 import part_one, part_two

sample_puzzle = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

# with open('day04/input.txt') as f:
#     live_puzzle_input = f.read().strip()
 

@pytest.mark.parametrize("puzzle_input,expected", [(sample_puzzle, 18)])
def test_part_one(puzzle_input, expected):

    actual = part_one(puzzle_input)

    assert actual == expected
