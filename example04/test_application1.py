"""
https://medium.com/@durgaswaroop/writing-better-tests-in-python-with-pytest-mock-part-2-92b828e1453c
"""
from application1 import get_operating_system


def test_get_operating_system(mocker):
    # Mock the slow function and return True always
    mocker.patch('application1.is_windows', return_value=True)
    assert get_operating_system() == 'Windows'


def test_operation_system_is_linux(mocker):
    # set the return value to be False
    mocker.patch('application1.is_windows', return_value=False)
    assert get_operating_system() == 'Linux'
