import unittest
from calculate_sum import calculate_sum

class TestCalculateSum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(calculate_sum(5, 3), 8)

    def test_negative_numbers(self):
        self.assertEqual(calculate_sum(-2, -7), -9)

    def test_zero(self):
        self.assertEqual(calculate_sum(0, 0), 0)

if __name__ == '__main__':
    unittest.main()
