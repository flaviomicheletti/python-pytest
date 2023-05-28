from unittest.mock import patch
from calculator1 import add


@patch("calculator1.add", return_value=9)
def test_add1(add):
    assert add(5, 5) == 9


def mock_add(x, y):
    return 11


@patch("calculator1.add", side_effect=mock_add)
def test_add2(add):
    assert add(5, 5) == 11

#
# 50%
#