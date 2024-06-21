from bank import value

def test_bank():
    assert value("hello sir") == 0
    assert value("sir") == 100
    assert value("HI sir") == 20
