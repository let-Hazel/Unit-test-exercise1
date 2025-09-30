import unittest
from main import factorial, fibonacci, fizzbuzz

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(fizzbuzz(3),[1,2, 'Fizz'])

        self.assertEqual(factorial(3), 6)

        self.assertEqual(fibonacci(6),(8, [0,1,1,2,3,5,8]))





if __name__ == "__main__":
    unittest.main()
