import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()


#
# Testing exceptions:
#
def perform_operation(value):
    if value < 0:
        raise ValueError("Negative value")
    elif value == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    else:
        return 10 / value


#
# Testing multiple exceptions:
#
def test_exceptions():
    with pytest.raises((ValueError, ZeroDivisionError)) as exc_info:
        perform_operation(-5)
    assert str(exc_info.value) == "Negative value"

    with pytest.raises((ValueError, ZeroDivisionError)) as exc_info:
        perform_operation(0)
    assert str(exc_info.value) == "Cannot divide by zero"

#
# Testing exception messages:
#


def validate_input(value):
    if not isinstance(value, int):
        raise ValueError("Input must be an integer")


def test_exception_message():
    with pytest.raises(ValueError, match="Input must be an integer"):
        validate_input("invalid")

#
# Testing absence of an exception:
#


def validate_condition(value):
    if not value:
        raise AssertionError("Condition not satisfied")


def test_no_exception():
    with pytest.raises(AssertionError):
        validate_condition(False)
