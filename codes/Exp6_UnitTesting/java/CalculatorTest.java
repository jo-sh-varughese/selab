// CalculatorTest.java  (JUnit 5)
import org.junit.jupiter.api.*;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {
    Calculator calc;

    @BeforeEach                       // like a pytest fixture
    void setUp() { calc = new Calculator(); }

    @Test
    void testAdd() { assertEquals(5, calc.add(2, 3)); }

    @ParameterizedTest                 // like pytest.mark.parametrize
    @CsvSource({"10,2,5", "9,3,3", "-8,2,-4"})
    void testDivide(int a, int b, int expected) {
        assertEquals(expected, calc.divide(a, b));
    }

    @Test
    void testDivideByZero() {          // like pytest.raises
        assertThrows(ArithmeticException.class, () -> calc.divide(5, 0));
    }
}
