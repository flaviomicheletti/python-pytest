from example09 import fetch_data

def test_fetch_data(mocker):
    # We create a mock object to replace requests.get
    mock_get = mocker.Mock()
    # We set the return_value for the mock object.
    mock_get.return_value.json.return_value = {'key': 'value'}
    # We use mocker.patch to replace the module function.
    mocker.patch('example09.requests.get', new=mock_get)

    assert fetch_data() == {'key': 'value'}
    # Ensure the mock was called correctly.
    mock_get.assert_called_once_with('https://example.com')
