# test_calculator.py - executes all Exp 5 test cases (ADD, SUB, MUL, DIV)
import pytest
from calculator import calculate

CASES = [
    # ---- Addition (manual) ----
    ('TC-ADD-01', 25, '+', 37, 62), ('TC-ADD-02', 50, '+', -20, 30),
    ('TC-ADD-03', -15, '+', -10, -25), ('TC-ADD-04', 0, '+', 99, 99),
    ('TC-ADD-05', 3.14, '+', 2.86, 6.0), ('TC-ADD-06', 999999998, '+', 1, 999999999),
    # ---- Subtraction ----
    ('TC-SUB-01', 50, '-', 20, 30), ('TC-SUB-02', 20, '-', 50, -30),
    ('TC-SUB-03', -10, '-', -25, 15), ('TC-SUB-04', 45, '-', 0, 45),
    ('TC-SUB-05', 5.75, '-', 2.25, 3.5), ('TC-SUB-06', 100, '-', 100, 0),
    ('TC-SUB-07', 50, '-', 'xyz', 'Error: Invalid input'),
    # ---- Multiplication ----
    ('TC-MUL-01', 12, '*', 8, 96), ('TC-MUL-02', 7, '*', -6, -42),
    ('TC-MUL-03', -5, '*', -4, 20), ('TC-MUL-04', 999, '*', 0, 0),
    ('TC-MUL-05', 2.5, '*', 1.5, 3.75), ('TC-MUL-06', 123, '*', 1, 123),
    ('TC-MUL-07', 99999, '*', 99999, 9999800001),
    ('TC-MUL-08', 'abc', '*', 3, 'Error: Invalid input'),
    # ---- Division (manual) ----
    ('TC-DIV-01', 100, '/', 4, 25), ('TC-DIV-02', 50, '/', 0, 'Error: Division by zero'),
    ('TC-DIV-03', 0, '/', 5, 0), ('TC-DIV-04', 10, '/', 3, 3.333333),
    ('TC-DIV-05', -20, '/', 4, -5), ('TC-DIV-06', 7.5, '/', 2.5, 3.0),
    ('TC-DIV-07', 'abc', '/', 5, 'Error: Invalid input'),
]

@pytest.mark.parametrize('tc,a,op,b,expected', CASES, ids=[c[0] for c in CASES])
def test_calculator(tc, a, op, b, expected):
    assert calculate(a, op, b) == expected
