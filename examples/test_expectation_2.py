import pytest


@pytest.mark.parametrize(
    "inputt,expected",
    [
        ("3+5", 8),
        ("2+4", 6),
        ("6*9", 42),
    ]
)
def test_eval(inputt, expected):
    assert eval(inputt) == expected
