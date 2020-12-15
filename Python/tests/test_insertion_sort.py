from code_challenges.insertion_sort import sort_insertion_temp, sort_insertion_swap

import pytest

def test_assert_sort_insertion_temp():
    assert sort_insertion_temp([8,4,23,42,16,15])

def test_sort_insertion_temp_empty_array():
    arr = []
    actual = sort_insertion_temp(arr)
    expected = []
    assert actual == expected

def test_sort_insertion_temp_simple_array():
    arr = [8,4,23,42,16,15]
    actual = sort_insertion_temp(arr)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_sort_insertion_temp_negative_array():
    arr = [8,4,23,42,16,15]
    actual = sort_insertion_temp(arr)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_sort_insertion_temp_unique_array():
    arr = [5,12,7,5,5,7]
    actual = sort_insertion_temp(arr)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_assert_sort_insertion_swap():
    assert sort_insertion_swap([8,4,23,42,16,15])

def test_sort_insertion_swap_empty_array():
    arr = []
    actual = sort_insertion_swap(arr)
    expected = []
    assert actual == expected

def test_sort_insertion_swap_simple_array():
    arr = [8,4,23,42,16,15]
    actual = sort_insertion_swap(arr)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_sort_insertion_swap_negative_array():
    arr = [8,4,23,42,16,15]
    actual = sort_insertion_swap(arr)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_sort_insertion_swap_unique_array():
    arr = [5,12,7,5,5,7]
    actual = sort_insertion_swap(arr)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected
