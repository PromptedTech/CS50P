import pytest
from twttr import shorten

def test_vowel_omitted():
    assert shorten('nakul') == "nkl"
    assert shorten('kabeer') == "kbr"
    assert shorten("shiva") == "shv"
    assert shorten("OM") == "M"
    assert shorten("hello, world") == "hll, wrld"
    assert shorten("") == ""
    
def test_int_error():
    with pytest.raises(TypeError):
        shorten(1)

def test_num():
    assert shorten("h3ll0") == "h3ll0"
    assert shorten("12345") == "12345"