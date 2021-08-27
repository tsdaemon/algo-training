import pytest

from preorder_binary_serialization.pre import Solution


@pytest.mark.parametrize(
    "preorder,valid",
    [
        ("9,3,4,#,#,1,#,#,2,#,6,#,#", True),
        ("1,#", False),
        ("9,#,#,1", False)
    ]
)
def test_basic(preorder, valid):
    s = Solution()
    assert s.isValidSerialization(preorder) == valid
