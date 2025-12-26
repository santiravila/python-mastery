from numb3rs import validate

def main():
    test_range()
    test_format()
    test_leading_zeros()


def test_range():
    assert validate(r"255.255.255.255") == True
    assert validate(r"512.255.255.255") == False
    assert validate(r"255.512.255.255") == False
    assert validate(r"255.255.512.255") == False
    assert validate(r"255.255.255.512") == False
    assert validate(r"512.512.512.512") == False


def test_leading_zeros():
    assert validate(r"01.2.3.4") == False
    assert validate(r"1.02.3.4") == False
    assert validate(r"1.2.03.4") == False
    assert validate(r"1.2.3.04") == False
    assert validate(r"01.02.03.04") == False


def test_format():
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1.2") == False
    assert validate(r"1") == False
    assert validate(r"1.2.3.4.5") == False


if __name__ == "__main__":
    main()
