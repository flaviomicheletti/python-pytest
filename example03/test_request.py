import requests


def get_data():
    response = requests.get("https://api.example.com/data")
    return response.json()


def test_get_data(mocker):
    # Patching the requests.get() function
    mock_get = mocker.patch("requests.get")

    # Mocking the return value of requests.get()
    mock_get.return_value.json.return_value = {"key": "value"}

    # Calling the function under test
    result = get_data()

    # Asserting the mock was called
    mock_get.assert_called_once_with("https://api.example.com/data")

    # Asserting the result
    assert result == {"key": "value"}
