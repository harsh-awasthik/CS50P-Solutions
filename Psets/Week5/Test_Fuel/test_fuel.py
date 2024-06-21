from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    with pytest.raises(ValueError):
        convert("cat/boy")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(75) == "75%"
