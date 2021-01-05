import pytest
from code_challenges.pascals_triangle.pascals_triangle import pascals_triangle

def test_import():
    assert pascals_triangle

def test_happy_path():
    actual = pascals_triangle(4)
    expected = [[1], [1,1], [1,2,1], [1,3,3,1]]
    assert actual == expected

def test_NAN():
    with pytest.raises(TypeError):
        pascals_triangle('f')
