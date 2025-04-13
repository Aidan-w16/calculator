import unittest
from model import Calculator

class Test_calculator(unittest.TestCase):

    def test_adding(self):
        calculator = Calculator()
        self.assertEqual(calculator.get_result(1,2,'+'), 3)
    
    def test_subtraction(self):
        calculator = Calculator()
        self.assertEqual(calculator.get_result(1,2,'-'), -1)
    
    def test_multiplication(self):
        calculator = Calculator()
        self.assertEqual(calculator.get_result(1,2,'X'),2)
    
    def test_division(self):
        calculator = Calculator()
        self.assertEqual(calculator.get_result(1,2,'/'),0.5)

if __name__ == '__main__':
    unittest.main()