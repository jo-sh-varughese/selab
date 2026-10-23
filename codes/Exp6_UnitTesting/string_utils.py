# string_utils.py
def is_palindrome(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    s = "".join(ch.lower() for ch in s if ch.isalnum())
    return s == s[::-1]

def is_leap(year):
    if year <= 0:
        raise ValueError("Year must be positive")
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
