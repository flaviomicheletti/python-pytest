#
# Testing instance-level variable in a class
#
class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 0


#
# Testing string content and attribute existence:
#

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "check"
        assert hasattr(x, "check") == False


#
# Testing class initialization and attributes:
#

class MyClass:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1

class TestClass1:
    def test_initialization(self):
        obj = MyClass(10)
        assert obj.value == 10

    def test_increment(self):
        obj = MyClass(5)
        obj.increment()
        assert obj.value == 6


#
# Testing class methods and behavior:
#

class Order:
    def __init__(self, items):
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def get_item_count(self):
        return len(self.items)

class TestClass2:
    def test_add_item(self):
        order = Order([])
        order.add_item("item1")
        order.add_item("item2")
        assert order.get_item_count() == 2

    def test_remove_item(self):
        order = Order(["item1", "item2", "item3"])
        order.remove_item("item2")
        assert order.get_item_count() == 2
