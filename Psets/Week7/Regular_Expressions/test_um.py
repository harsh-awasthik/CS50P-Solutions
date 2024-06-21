from um import count

def test_count1():
    assert count("um i want sum") == 1
    assert count("umm") == 0

def test_count2():
    assert count("hello um my name is um, harsh") == 2

def test_count3():
    assert count("Um, my Um um is umm") == 3
