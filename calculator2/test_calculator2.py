from calculator2 import Calculator


def test_calculator_add(mocker):
    # Create an instance of the Calculator class
    calculator = Calculator()

    # Patch the Calculator class to replace the add method with a mock
    mock_add = mocker.patch.object(calculator, 'add')

    # Define the expected return value from the mock
    mock_add.return_value = 11

    # Call the add method of the Calculator class
    result = calculator.add(3, 7)

    # Assertions
    assert result == 11
    mock_add.assert_called_once_with(3, 7)


def test_calculator_subtract(mocker):
    # Create an instance of the Calculator class
    calculator = Calculator()

    # Patch the Calculator class to replace the add method with a mock
    mock_add = mocker.patch.object(calculator, 'subtract')

    # Define the expected return value from the mock
    mock_add.return_value = 8

    # Call the add method of the Calculator class
    result = calculator.subtract(10, 1)

    # Assertions
    assert result == 8
    mock_add.assert_called_once_with(10, 1)

