import windows_utils


def get_operating_system():
    return "Windows" if windows_utils.is_windows() else "Linux"
