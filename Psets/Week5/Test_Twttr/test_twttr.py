from twttr import shorten

def test_shorten():
    assert(shorten("harsh")) == "hrsh"
    assert(shorten("awasthi")) == "wsth"
    assert(shorten("Awasthi")) == "wsth"
    assert(shorten("hello harsh 123!")) == "hll hrsh 123!"

