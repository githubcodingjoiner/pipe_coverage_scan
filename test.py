import unittest
from fib import generate_fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_5_terms(self):
        self.assertEqual(generate_fibonacci(5), [0, 1, 1, 2, 3])

    def test_fibonacci_1_term(self):
        self.assertEqual(generate_fibonacci(1), [0])

    def test_fibonacci_0_terms(self):
        self.assertEqual(generate_fibonacci(0), [])

    def test_fibonacci_large_input(self):
        self.assertEqual(generate_fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

if __name__ == "__main__":
    unittest.main()
