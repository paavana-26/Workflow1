from c import add, subtract, multiply, divide

def test_add():
    assert add(10, 5) == 15

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(10, 5) == 50

def test_divide():
    assert divide(10, 5) == 2
    assert divide(10, 0) == "Error! Division by zero."
test_add()
test_subtract()
test_multiply()
test_divide()
