import unittest
from calculator import add, sub, mul, div

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_sub(self):
        self.assertEqual(sub(10, 5), 5)

    def test_mul(self):
        self.assertEqual(mul(10, 5), 50)

    def test_div(self):
        self.assertEqual(div(10, 5), 2)

if __name__ == "__main__":
    unittest.main()