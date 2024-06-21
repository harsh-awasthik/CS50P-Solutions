from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(2)
    assert jar.size == 2


def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(2)
    assert jar.size == 1
