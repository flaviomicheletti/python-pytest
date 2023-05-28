import pytest


def test_set_mock_behavior(mocker):
    """You can define the behavior of the mock object using its methods,
    attributes, or return values. For example:"""

    # Create a mock object
    mock_obj = mocker.Mock()

    # Set a method return value
    mock_obj.some_method.return_value = 42

    # Set an attribute value
    mock_obj.some_attribute = 'test'

    # Set a side effect (executes a function when the method is called)
    mock_obj.some_method.side_effect = lambda x: x + 1

    assert mock_obj.some_method(1) == 2


def test_use_the_mock(mocker):
    """Utilize the mock object in your test logic, 
    asserting that it's called correctly or inspecting its behavior:"""

    def some_function_that_uses_mock(param):
        return param.some_method()

    # Create a mock object
    mock_obj = mocker.Mock()

    # Set a method return value
    mock_obj.some_method.return_value = 42

    # Use the mock object
    result = some_function_that_uses_mock(mock_obj)

    # Assert the result
    assert result == 42

    # Assert that the mock method was called
    mock_obj.some_method.assert_called_once()


def test_mocking_functions_methods(mocker):
    """pytest-mock provides the mocker.Mock() object, 
    which can be used to mock functions and methods. 
    You can define return values, side effects, 
    and assert method calls just like in the previous example."""

    def some_function_that_uses_mock_func(param):
        return param()

    # Create a mock function
    mock_func = mocker.Mock(return_value=42)

    # Use the mock function
    result = some_function_that_uses_mock_func(mock_func)

    # Assert the result
    assert result == 42

    # Assert that the mock function was called
    mock_func.assert_called_once()




