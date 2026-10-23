# grade_calculator.py
# Module: Student Grade Calculator (Exp 6 - lab manual)

def calculate_grade(marks):
    """Return letter grade for given marks (0-100)."""
    if not isinstance(marks, (int, float)):
        raise TypeError('Marks must be a number')
    if marks < 0 or marks > 100:
        raise ValueError('Marks must be between 0 and 100')
    if marks >= 90:   return 'O'      # Outstanding
    elif marks >= 80: return 'A+'
    elif marks >= 70: return 'A'
    elif marks >= 60: return 'B+'
    elif marks >= 50: return 'B'
    elif marks >= 40: return 'C'
    else:             return 'F'      # Fail

def is_pass(marks):
    """Return True if student has passed (grade is not F)."""
    return calculate_grade(marks) != 'F'

def calculate_cgpa(grades):
    """
    Calculate CGPA from list of (marks, credit) tuples.
    Example: [(85, 4), (92, 3), (75, 4)]
    """
    if not grades:
        raise ValueError('Grade list cannot be empty')
    gp = {'O': 10, 'A+': 9, 'A': 8, 'B+': 7, 'B': 6, 'C': 5, 'F': 0}
    total_points = sum(gp[calculate_grade(m)] * c for m, c in grades)
    total_credits = sum(c for _, c in grades)
    return round(total_points / total_credits, 2)
