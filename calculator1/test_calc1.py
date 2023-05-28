import pytest
from unittest.mock import patch
from calculator1 import add

def test_add():
    with patch('calculator1.time.sleep', return_value=None) as mock_sleep:
        result = add(2, 3)
        mock_sleep.assert_called_once_with(5)
        assert result == 5

#
# 100%
#