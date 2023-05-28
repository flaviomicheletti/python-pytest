import pytest
from calculator import calculate_sum, Calculator


def test_calculate_sum(mocker):
    # Create a mock object
    mock_add = mocker.patch.object(Calculator, 'add')

    # Set the return value for the mocked method
    mock_add.return_value = 10

    # Call the function under test
    result = calculate_sum()

    # Assert that the mocked method was called
    assert mock_add.called

    # Assert the result
    assert result == 10