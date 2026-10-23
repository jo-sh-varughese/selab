# test_grade_calculator.py
import pytest
from grade_calculator import calculate_grade, is_pass, calculate_cgpa

# -- FIXTURE ----------------------------------------------------------
@pytest.fixture
def sample_grades():
    """Reusable sample list: [(marks, credits), ...]"""
    return [(85, 4), (92, 3), (75, 4), (60, 3)]

# -- CLASS 1: Basic Grade Tests ---------------------------------------
class TestCalculateGrade:

    def test_outstanding(self):
        # Arrange
        marks = 95
        # Act
        result = calculate_grade(marks)
        # Assert
        assert result == 'O', f'Expected O, got {result}'

    def test_fail(self):
        assert calculate_grade(30) == 'F'

    def test_pass_fail_boundary(self):
        assert calculate_grade(40) == 'C'     # just passes
        assert calculate_grade(39) == 'F'     # just fails

    def test_outstanding_boundary(self):
        assert calculate_grade(90) == 'O'     # min of O
        assert calculate_grade(89) == 'A+'    # max of A+

    # -- PARAMETRISED: all grade boundaries --------------------------
    @pytest.mark.parametrize('marks,expected', [
        (100, 'O'), (90, 'O'), (89, 'A+'), (80, 'A+'), (79, 'A'), (70, 'A'),
        (69, 'B+'), (60, 'B+'), (59, 'B'), (50, 'B'), (49, 'C'), (40, 'C'),
        (39, 'F'), (0, 'F'),
    ])
    def test_all_boundaries(self, marks, expected):
        assert calculate_grade(marks) == expected

# -- CLASS 2: Exception Tests -----------------------------------------
class TestExceptions:

    def test_above_100(self):
        with pytest.raises(ValueError, match='between 0 and 100'):
            calculate_grade(101)

    def test_negative(self):
        with pytest.raises(ValueError):
            calculate_grade(-1)

    def test_string_input(self):
        with pytest.raises(TypeError, match='must be a number'):
            calculate_grade('eighty')

# -- CLASS 3: CGPA Tests (uses fixture) -------------------------------
class TestCGPA:

    def test_returns_float(self, sample_grades):
        result = calculate_cgpa(sample_grades)
        assert isinstance(result, float)
        assert 0.0 <= result <= 10.0

    def test_sample_value(self, sample_grades):
        assert calculate_cgpa(sample_grades) == 8.5   # (36+30+32+21)/14

    def test_empty_list_raises(self):
        with pytest.raises(ValueError):
            calculate_cgpa([])

    def test_all_outstanding(self):
        grades = [(95, 3), (92, 4), (91, 3)]
        assert calculate_cgpa(grades) == 10.0

# -- CLASS 4: is_pass Tests -------------------------------------------
class TestIsPass:

    def test_pass(self):
        assert is_pass(50) == True

    def test_fail(self):
        assert is_pass(35) == False

    def test_exact_pass_mark(self):
        assert is_pass(40) == True

# -- RUN COMMANDS -----------------------------------------------------
# pytest test_grade_calculator.py -v
# pytest test_grade_calculator.py -v --cov=grade_calculator --cov-report=term-missing
