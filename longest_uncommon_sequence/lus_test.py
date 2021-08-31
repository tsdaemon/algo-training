from typing import List
import pytest

from longest_uncommon_sequence.lus import Solution


@pytest.mark.parametrize(
    "input,output",
    [
        (["aba","cdc","eae"], 3),
        (["aaa","aaa","aa"], -1),
        (["aabbcc", "aabbcc", "cb", "abc"], 2)
    ]
)
def test_basic(input: List[str], output: int):
    s = Solution()
    actual_output = s.findLUSlength(input)
    assert actual_output == output
    