import pytest

from combination_sum.combination_sum import Solution


@pytest.mark.parametrize(
    'candidates,target,expected_result',
    [
        ([2,3,6,7], 7, [[2,2,3],[7]]),
        ([2,3,5], 8, [[2,2,2,2],[2,3,3],[3,5]]),
    ]
)
def test_basic(candidates, target, expected_result):
    s = Solution()
    result = s.combinationSum(candidates, target)
    assert result == expected_result
