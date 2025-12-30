from seasons import minutes_from_birth, sing_minutes, validate
import pytest
from datetime import date

def test_validation():
    with pytest.raises(ValueError):
        validate("January 1, 1999")


def test_conversion():
    assert minutes_from_birth(date(1999, 1, 1)) == 14198400


def test_output():
    assert sing_minutes(14198400) == "Fourteen million, one hundred ninety-eight thousand, four hundred"