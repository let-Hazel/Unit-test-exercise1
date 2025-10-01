import unittest
from main import factorial, fibonacci, fizzbuzz

class TestMain(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(3), 6)
        self.assertNotEqual(factorial(-1), "input positive number")
        self.assertEqual(factorial(0), 1)
        # self.assertRaises(NameError,fibonacci, n)
        self.assertRaises(ValueError, fibonacci, "n")
        


    def test_fibonacci(self):
        self.assertEqual(fibonacci(6),[8, [0,1,1,2,3,5,8]])
        self.assertEqual(fibonacci(-1), "only positive integers")
        self.assertEqual(fibonacci(1), "only numbers above 1")
        # self.assertRaises(NameError, fibonacci(p))
        self.assertRaises(ValueError, fibonacci, "p")

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(3),[1,2, 'Fizz'])
        self.assertEqual(fizzbuzz(5),[1, 2, 'Fizz', 4, 'Buzz'])
        self.assertEqual(fizzbuzz(15),[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz'])
        # self.assertRaises(ValueError, fizzbuzz, "f")


if __name__ == "__main__":
    unittest.main()
