import unittest
#from app import calculator
from app.calculator import Calculator

class CalculatorTests(unittest.TestCase):

    def test_add_positive(self):
        calculator = Calculator(10, 20)
        result = calculator.add()
        self.assertEqual(result, 30)

    def test_add_negative(self):
        calculator = Calculator(-10, -20)
        result = calculator.add()
        self.assertEqual(result, -30)

    def test_subtract_positive(self):
        calculator = Calculator(10, 20)
        result = calculator.subtract()
        self.assertEqual(result, -10)

    def test_subtract_negative(self):
        calculator = Calculator(-10, -20)
        result = calculator.subtract()
        self.assertEqual(result, 10)

    def test_multiply_positive(self):
        calculator = Calculator(10, 20)
        result = calculator.multiply()
        self.assertEqual(result, 200)

    def test_multiply_negative(self):
        calculator = Calculator(-10, -20)
        result = calculator.multiply()
        self.assertEqual(result, 200)

    def test_divide_positive(self):
        calculator = Calculator(10, 20)
        result = calculator.divide()
        self.assertEqual(result, 0.5)

    def test_divide_by_zero(self):
        calculator = Calculator(10, 0)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide()

    def test_power_positive(self):
        calculator = Calculator(10, 2)
        result = calculator.power()
        self.assertEqual(result, 100)

    def test_power_negative(self):
        calculator = Calculator(10, -2)
        result = calculator.power()
        self.assertEqual(result, 0.01)

    def test_random_number(self):
        result = Calculator.random_number(1, 100)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 100)


if __name__ == "__main__":
    unittest.main()
