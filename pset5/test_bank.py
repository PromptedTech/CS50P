import pytest
from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("hello there") == 0


def test_h():
    assert value("howdy") == 20
    assert value("hey!") == 20
    assert value("hi!") == 20


def test_other():
    assert value("yo") == 100
    assert value("whats up") == 100
    assert value("good morning") == 100
    assert value("welcome") == 100


def test_case_insensitivity():
    assert value("HELLO") == 0
    assert value("Hey") == 20
    assert value("GOOD MORNING") == 100


def test_num():
    with pytest.raises(AttributeError):
        value(1)