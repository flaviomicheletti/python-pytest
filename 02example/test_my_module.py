from my_module import my_function, MyClass


def test_my_function(mocker):
    # Create a mock object
    mock_method = mocker.patch.object(MyClass, 'method')

    # Set the return value for the mocked method
    mock_method.return_value = "Mocked method"

    # Call the function under test
    result = my_function()

    # Assert that the mocked method was called
    assert mock_method.called

    # Assert the result
    assert result == "Mocked method"
