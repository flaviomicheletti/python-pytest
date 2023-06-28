# Docs

## assertions

While `self.assert` is commonly used in testing with the built-in unittest 
module, Pytest uses a different syntax for assertions. However, Pytest provides 
a number of built-in assertion methods that you can use instead.

These built-in assertion methods are similar to `self.assert` in that they 
allow you to check that a given condition is true, and they provide informative
error messages if the assertion fails. Here are some examples:

    assert x == y: Checks that x is equal to y.
    assert x != y: Checks that x is not equal to y.
    assert x in y: Checks that x is a member of y.
    assert x not in y: Checks that x is not a member of y.
    assert x is y: Checks that x and y refer to the same object.
    assert x is not y: Checks that x and y do not refer to the same object.
    assert x > y: Checks that x is greater than y.
    assert x < y: Checks that x is less than y.
    assert x >= y: Checks that x is greater than or equal to y.
    assert x <= y: Checks that x is less than or equal to y.


## Pytest-mock

- https://pytest-mock.readthedocs.io/en/latest/index.html

`pytest-mock` is a plugin for the pytest testing framework that provides 
powerful mocking capabilities. It allows you to easily create and manage 
mocks, stubs, and spies in your test cases. Here are some of the ways you can 
use `pytest-mock`: 

1. Creating mocks: You can use `mocker.Mock()` or `mocker.MagicMock()` to 
create mock objects. These mocks can be used to replace dependencies and 
simulate their behavior during testing. 

2. Patching objects: `pytest-mock` provides the `mocker.patch()` decorator 
and the `mocker.patch.object()` context manager to patch objects and replace 
them with mocks. This is useful when you want to mock external dependencies 
or modify the behavior of specific objects during testing. 

3. Stubbing functions: `pytest-mock` allows you to stub functions using the `
mocker.stub()` method. Stubs are lightweight objects that can be used to 
replace function implementations temporarily. 

4. Checking calls: You can use `mocker.call_count` and `mocker.call_args` to 
check how many times a mock has been called and what arguments it was called 
with. This helps you verify the interactions between your code and the mocks. 

5. Side effects: `pytest-mock` provides the `mocker.side_effect` attribute, 
which allows you to define custom behaviors for mocks. You can raise 
exceptions, return different values, or execute arbitrary code when the mock 
is called. 

6. Spies: `pytest-mock` supports spies, which are mocks that record calls to 
real objects while still allowing the original behavior. You can use `
mocker.spy()` to create a spy object and then assert on its calls or examine 
the recorded data. 

7. Patching context managers: If you need to mock a context manager, `pytest-
mock` provides the `mocker.patch.object()` context manager, which can be used 
to replace the behavior of the `__enter__()` and `__exit__()` methods. 

These are just some of the ways you can use `pytest-mock` to enhance your 
testing workflow. The plugin offers many more features and utilities, so I 
encourage you to refer to the official documentation for more detailed 
examples and instructions.