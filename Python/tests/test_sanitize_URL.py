import pytest
from code_challenges.sanitize_URL.sanitize_URL import sanitize_URL

def test_no_input():
    with pytest.raises(TypeError):
        sanitize_URL()

def test_happy_path():
    actual = sanitize_URL("http://code.org/hour of code.html")
    expected = "http://code.org/hour%20of%20code.html"
    assert actual == expected

def test_bad_URL():
    actual = sanitize_URL("htp://code.org/hour of code.html")
    expected = "Invalid URL format"
    assert actual == expected

def test_no_spaces():
    actual = sanitize_URL("http://code.org/hourofcode.html")
    expected = "http://code.org/hourofcode.html"
    assert actual == expected
