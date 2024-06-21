from numb3rs import validate

def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True

def test_for255plus():
    assert validate("1.2.3.1000") == False
    assert validate("512.512.512.512") == False

def test_forip():
    assert validate("cat") == False

def test_forfirstbyte():
    assert validate("55.265.655.655") == False
