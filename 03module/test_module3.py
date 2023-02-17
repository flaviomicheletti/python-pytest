#
# https://pytest-mock.readthedocs.io/
#

import os


class UnixFS:
    @staticmethod
    def rm(filename):
        os.remove(filename)


def test_unix_fs(mocker):
    mocker.patch("os.remove")
    UnixFS.rm("file")
    os.remove.assert_called_once_with("file")


def test_all(mocker):
    # all valid calls
    mocker.patch("os.remove")
    mocker.patch.object(os, "listdir", autospec=True)
    mocked_isfile = mocker.patch("os.path.isfile")
