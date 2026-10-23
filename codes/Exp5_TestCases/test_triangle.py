# test_triangle.py - EP + BVA (4n+1 = 13) test cases
import pytest
from triangle import classify_triangle as ct

EP = [
    ('TC-TRI-01', (5, 5, 5), 'Equilateral'), ('TC-TRI-02', (5, 5, 3), 'Isosceles'),
    ('TC-TRI-03', (3, 4, 5), 'Scalene'), ('TC-TRI-04', (2, 3, 5), 'Not a triangle'),
    ('TC-TRI-05', (1, 2, 10), 'Not a triangle'), ('TC-TRI-06', (0, 4, 5), 'Invalid input'),
    ('TC-TRI-07', (101, 50, 60), 'Invalid input'), ('TC-TRI-08', ('a', 4, 5), 'Invalid input'),
]
@pytest.mark.parametrize('tc,sides,expected', EP, ids=[e[0] for e in EP])
def test_ep(tc, sides, expected):
    assert ct(*sides) == expected

BVA = [((1,50,50),'Isosceles'),((2,50,50),'Isosceles'),((50,50,50),'Equilateral'),
       ((99,50,50),'Isosceles'),((100,50,50),'Not a triangle'),
       ((50,1,50),'Isosceles'),((50,2,50),'Isosceles'),((50,99,50),'Isosceles'),((50,100,50),'Not a triangle'),
       ((50,50,1),'Isosceles'),((50,50,2),'Isosceles'),((50,50,99),'Isosceles'),((50,50,100),'Not a triangle')]
@pytest.mark.parametrize('sides,expected', BVA)
def test_bva(sides, expected):
    assert ct(*sides) == expected
