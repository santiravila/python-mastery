from um import count


def test_format():
    assert count("uum and umm") == 0


def test_case():
    assert count("Um, testing uM") == 2


def test_punct():
    assert count("abs ...um... Um              um") == 3


def test_word():
    assert count("humane and luminiscent") == 0
