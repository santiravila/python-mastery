from bank import value


def test_h():
    assert value("Hi friend") == 20


def test_hello():
    assert value("Hello, mister") == 0


def test_none():
    assert value("What's up!") == 100


