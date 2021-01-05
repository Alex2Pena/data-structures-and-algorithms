import pytest
from code_challenges.is_anagram.is_anagram import is_anagram

def test_import():
    assert is_anagram

def test_none():
    with pytest.raises(TypeError):
        is_anagram()

def test_empty():
    actual = is_anagram("","")
    expected = True
    assert actual == expected

def test_true():
    actual = is_anagram("Eleven plus two", "Twelve plus one")
    expected = True
    assert actual == expected

def test_false():
    actual = is_anagram("Software", "Swear often")
    expected = False
    assert actual == expected
