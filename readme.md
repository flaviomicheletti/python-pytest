![image](https://user-images.githubusercontent.com/1257048/204163799-a6a9e866-1ca8-4c72-8cf5-26217e3526c5.png)

# A short practical guide to testing Python (pytest)

A little guide to help you test your Python code with framework __pytest__.

https://docs.pytest.org/


__venve:__

    python3 -m venv .venv && . .venv/bin/activate

__libs:__

In both environments you will need to install it only once.

    pip install -U pytest
    pip install pytest-mock
    pip install requests

__running:__

    pytest

__coverage:__

    coverage run -m pytest
    coverage html


__coverage(pytest-cov):__

- https://pytest-cov.readthedocs.io/en/latest/

    pytest --cov . --cov-report html
