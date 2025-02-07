# tests/test_main.py

import pytest
from my_app.main import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(10.5, 4.5) == 15.0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(2, 5) == -3

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 3) == -3

def test_divide():
    assert divide(6, 3) == 2
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
