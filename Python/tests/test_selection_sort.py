from code_challenges.merge_sort.merge_sort import merge_sort

def test_assert_selection_sort():
    assert merge_sort([8,4,23,42,16,15])

def test_merge_sort_empty_array():
    arr = []
    actual = merge_sort(arr)
    expected = None
    assert actual == expected

def test_merge_sort_simple_array():
    arr = [8,4,23,42,16,15]
    actual = merge_sort(arr)
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_merge_sort_negative_array():
    arr = [8,4,23,42,-16,15]
    actual = merge_sort(arr)
    expected = [-16,4,8,15,23,42]
    assert actual == expected

def test_merge_sort_unique_array():
    arr = [5,12,7,5,5,7]
    actual = merge_sort(arr)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected
