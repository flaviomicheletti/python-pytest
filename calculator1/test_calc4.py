import calculator1


def test_add(mocker):
    # Patch the add function with a mock
    mock_add = mocker.patch('calculator1.add')

    # Define the expected return value from the mock
    mock_add.return_value = 10

    # Call the add function
    result = calculator1.add(3, 7)

    # Assertions
    assert result == 10
    mock_add.assert_called_once_with(3, 7)
    
#
# 50%
#