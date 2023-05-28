![image](https://user-images.githubusercontent.com/1257048/204163799-a6a9e866-1ca8-4c72-8cf5-26217e3526c5.png)

# A short practical guide to testing Python (pytest)

A little guide to help you test your Python code with framework __pytest__.

https://docs.pytest.org/


# Instalation

    python3 -m venv .venv && . .venv/bin/activate

## Install

In both environments you will need to install it only once.

    pip install -U pytest
    pip install pytest-mock
    pip install requests

## Running

    pytest


## Coverage

    coverage run -m pytest
    coverage html

##  COverage - pytest-cov

    pytest --cov . --cov-report html
