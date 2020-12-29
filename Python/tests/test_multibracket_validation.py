from code_challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation


def test_no_input():
    actual = multi_bracket_validation(None)
    expected = TypeError
    assert actual == expected

def test_empty_string():
    actual = multi_bracket_validation('')
    expected = TypeError
    assert actual == expected

def test_happy_path():
    actual = multi_bracket_validation('{[(a({["k(fdsbcjehw[{}]vjhcew)k"]})?)]}')
    expected = True
    assert actual == expected

def test_false_input():
    actual = multi_bracket_validation('{[(a({["k(fdsbc)jehw[{}]vjhcew)k"]})?)]}')
    expected = False
    assert actual == expected

def test_begining_false():
    actual = multi_bracket_validation('{{[(a({["k(fdsbcjehw[{}]vjhcew)k"]})?)]}')
    expected = False
    assert actual == expected

def test_ending_false():
    actual = multi_bracket_validation('{[(a({["k(fdsbcjehw[{}]vjhcew)k"]})?)]}}')
    expected = False
    assert actual == expected
