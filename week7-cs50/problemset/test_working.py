import pytest
from working import convert


def test_range():
    with pytest.raises(ValueError):
        convert("12:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("13:30 AM to 4:00 PM")
    with pytest.raises(ValueError):
        convert("5:00 AM to 13:15 PM")


def test_variations():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"


def test_format():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("this to that")