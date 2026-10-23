# triangle.py - classic triangle classification problem (Exp 5 similar question)
def classify_triangle(a, b, c):
    for s in (a, b, c):
        if isinstance(s, bool) or not isinstance(s, int) or not 1 <= s <= 100:
            return 'Invalid input'
    if a >= b + c or b >= a + c or c >= a + b:
        return 'Not a triangle'
    if a == b == c:
        return 'Equilateral'
    if a == b or b == c or a == c:
        return 'Isosceles'
    return 'Scalene'
