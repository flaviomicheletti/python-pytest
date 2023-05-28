import requests


def test_get_random_dog(mocker):
    # This is the response we want the mocked function to return.
    fake_response = {
        'message': 'https://images.dog.ceo/breeds/retriever-chesapeake/n02099849_1024.jpg',
        'status': 'success'
    }

    # We use mocker.patch to replace the function requests.get.
    mocker.patch('requests.get', return_value=fake_response)

    response = requests.get('https://dog.ceo/api/breeds/image/random')

    # Now the response of requests.get will be the fake_response we declared above.
    assert response == fake_response


def fetch_data():
    response = requests.get('https://example.com')
    return response.json()


def test_fetch_data(mocker):
    # We create a mock object to replace requests.get
    mock_get = mocker.Mock()
    # We set the return_value for the mock object.
    mock_get.return_value.json.return_value = {'key': 'value'}
    # We use mocker.patch to replace the module function.
    mocker.patch('requests.get', new=mock_get)

    assert fetch_data() == {'key': 'value'}
    # Ensure the mock was called correctly.
    mock_get.assert_called_once_with('https://example.com')
