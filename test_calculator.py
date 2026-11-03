import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(10,5), 15)
    # Add the following test methods to the TestCalculator class:
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10,2), 8)
        self.assertEqual(self.calc.subtract(-20,2), -22)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4,-3), -12)
        self.assertEqual(self.calc.multiply(50,2), 100)
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(7, 0), 0)
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)
        self.assertEqual(self.calc.modulo(10, 3), 1)
    
    
if __name__ == '__main__':
    unittest.main()