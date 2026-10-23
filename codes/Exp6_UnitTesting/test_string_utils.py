# test_string_utils.py
import pytest
from string_utils import is_palindrome, is_leap

@pytest.mark.parametrize("text,expected", [
    ("madam", True), ("Madam", True), ("A man, a plan, a canal: Panama", True),
    ("hello", False), ("", True), ("a", True),
])
def test_palindrome(text, expected):
    assert is_palindrome(text) == expected

def test_palindrome_non_string():
    with pytest.raises(TypeError):
        is_palindrome(121)

@pytest.mark.parametrize("year,expected", [
    (2024, True), (2023, False), (1900, False), (2000, True),
])
def test_leap(year, expected):
    assert is_leap(year) == expected

def test_leap_invalid():
    with pytest.raises(ValueError):
        is_leap(0)
