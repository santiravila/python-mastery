from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(5)
    assert jar.capacity == 5


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪" 


def test_deposit():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.deposit(6)
    jar = Jar(13)
    with pytest.raises(ValueError):
        jar.deposit(14)
    jar.deposit(6)
    assert jar.size == 6

def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2