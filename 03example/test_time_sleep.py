import time


def perform_task():
    time.sleep(5)
    return "Task completed"


def test_perform_task(mocker):
    # Patching the time.sleep() function
    mock_sleep = mocker.patch("time.sleep")

    # Calling the function under test
    result = perform_task()

    # Asserting the mock was called with the expected argument
    mock_sleep.assert_called_once_with(5)

    # Asserting the result
    assert result == "Task completed"
