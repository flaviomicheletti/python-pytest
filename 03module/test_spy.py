import pytest

def test_spy_method(mocker):
    class Foo(object):
        def bar(self, v):
            return v * 2

    foo = Foo()
    spy = mocker.spy(foo, "bar")
    assert foo.bar(21) == 42

    spy.assert_called_once_with(21)
    assert spy.spy_return == 42

@pytest.mark.skip(reason="no way of currently testing this")
def test_spy_function(mocker):
    # mymodule declares `myfunction` which just returns 42
    import mymodule

    spy = mocker.spy(mymodule, "myfunction")
    assert mymodule.myfunction() == 42
    assert spy.call_count == 1
    assert spy.spy_return == 42


def test_with_unspy(mocker):
    class Foo:
        def bar(self):
            return 42

    spy = mocker.spy(Foo, "bar")
    foo = Foo()
    assert foo.bar() == 42
    assert spy.call_count == 1
    mocker.stop(spy)
    assert foo.bar() == 42
    assert spy.call_count == 1

def test_stub(mocker):
    def foo(on_something):
        on_something('foo', 'bar')

    stub = mocker.stub(name='on_something_stub')

    foo(stub)
    stub.assert_called_once_with('foo', 'bar')    