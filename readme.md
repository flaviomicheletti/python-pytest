![image](https://user-images.githubusercontent.com/1257048/204163799-a6a9e866-1ca8-4c72-8cf5-26217e3526c5.png)

# A short practical guide to testing Python (pytest)

A little guide to help you test your Python code with framework __pytest__.

https://docs.pytest.org/


# Instalation

__venv:__

    python3 -m venv venv
    . venv/bin/activate

    // in the first time
    pip install -U pytest

__virtualenv:__

    virtualenv .
    source bin/activate
    pip install --upgrade pip
    pip install mock
    deactivate


## Running

    pytest
