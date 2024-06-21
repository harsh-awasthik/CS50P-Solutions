from working import convert
import pytest

def test_convert1():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
        convert("cat")

def test_convert2():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_convert3():
    with pytest.raises(ValueError):
        convert("13 AM to 14 PM")

