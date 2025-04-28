import unittest
from calculate_sum import calculate_sum


class TestCalculateSum(unittest.TestCase):
    """
    Test cases for the calculate_sum function.
    """

    def test_positive_numbers(self):
        """
        Test case: Adding two positive numbers.
        """
        self.assertEqual(calculate_sum(5, 3), 8)

    def test_negative_numbers(self):
        """
        Test case: Adding two negative numbers.
        """
        self.assertEqual(calculate_sum(-2, -7), -9)

    def test_zero(self):
        """
        Test case: Adding two zeros.
        """
        self.assertEqual(calculate_sum(0, 0), 0)


if __name__ == '__main__':
    unittest.main()