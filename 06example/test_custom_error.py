import pytest


class CustomError(Exception):
    pass


def divide(a, b):
    if b == 0:
        raise CustomError("Cannot divide by zero")
    return a / b


def test_divide():
    with pytest.raises(CustomError) as exc_info:
        divide(10, 0)

    # Accessing the raised exception
    assert str(exc_info.value) == "Cannot divide by zero"
