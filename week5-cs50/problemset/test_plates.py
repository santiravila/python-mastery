from plates import is_valid


def test_validity():
    assert is_valid("HELLO") == True
    assert is_valid("CS50") == True


def test_punctuation():
    assert is_valid("HELLO, WORLD") == False
    assert is_valid("WORLD!") == False
    assert is_valid("Plate 30") == False


def test_length():
    assert is_valid("GOODBYE") == False


def test_numbers():
    assert is_valid("CS05") == False
    assert is_valid("ABC5D") == False


