import unittest
from simple_calculator import SimpleCalculator  # Import the SimpleCalculator class

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -5), -10)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(5, 10), -5)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-4, 5), -20)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-3, -3), 9)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertIsNone(self.calc.divide(10, 0))  # Test division by zero

    def test_edge_cases(self):
        """Test edge cases for all methods."""
        self.assertEqual(self.calc.add(1e9, 1e9), 2e9)  # Large numbers
        self.assertEqual(self.calc.subtract(1e9, 1e9), 0)
        self.assertEqual(self.calc.multiply(1e9, 1e9), 1e18)
        self.assertEqual(self.calc.divide(1e9, 1e6), 1e3)
        self.assertIsNone(self.calc.divide(1, 0))  # Division by zero

if __name__ == "__main__":
    unittest.main()
