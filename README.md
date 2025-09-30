# Python Algorithm Functions

This repository contains a set of Python functions that implement common algorithms and programming challenges. Your task is to implement and thoroughly test each function, including edge cases.

## Functions to Implement

### 1. `factorial(n)`
**Description:** Calculates the factorial of a non-negative integer.

- Returns the factorial of n (n!)
- Should handle edge cases like 0! = 1
- Should raise appropriate errors for negative numbers

**Examples:**
```python
factorial(0)   # -> 1
factorial(1)   # -> 1
factorial(5)   # -> 120
factorial(10)  # -> 3628800
```

### 2. `fibonacci(n)`
**Description:** Returns the nth number in the Fibonacci sequence.

- The Fibonacci sequence starts with 0, 1, 1, 2, 3, 5, 8, 13...
- Should handle edge cases for n = 0 and n = 1

**Examples:**
```python
fibonacci(0)   # -> 0
fibonacci(1)   # -> 1
fibonacci(5)   # -> 5
fibonacci(10)  # -> 55
```

### 3. `fizzbuzz(n)`
**Description:** Returns a list for the FizzBuzz game up to n.

- Multiples of 3 are "Fizz"
- Multiples of 5 are "Buzz"
- Multiples of both 3 and 5 are "FizzBuzz"
- All other numbers remain as integers

**Examples:**
```python
fizzbuzz(15)  # -> [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
fizzbuzz(5)   # -> [1, 2, "Fizz", 4, "Buzz"]
```

## Instructions

1. **Implement all functions** in the main Python file (`main.py`).

2. **Write comprehensive tests** for all functions, including edge cases, such as:
   - Negative numbers for factorial
   - Large numbers for fibonacci
   - Edge cases like n=0 and n=1
   - Invalid inputs

3. **Place all test cases** in a separate file: `tests/test.py`

4. **Use Python's built-in unittest framework** for testing. Example:

```python
import unittest
from main import factorial, fibonacci, fizzbuzz

class TestAlgorithmFunctions(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)

    def test_fibonacci_base_cases(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_fizzbuzz_basic(self):
        result = fizzbuzz(5)
        expected = [1, 2, "Fizz", 4, "Buzz"]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
```

5. **Ensure all tests pass** before submission.

## Getting Started

### Prerequisites

- Python 3.6 or higher

### Running the Functions

```bash
python main.py
```

### Running Tests

```bash
python -m unittest tests.test
```

Or run tests with verbose output:

```bash
python -m unittest tests.test -v
```

## Project Structure

```text
Unit-test-exercise1/
├── main.py           # Main implementation file
├── tests/
│   └── test.py       # Test cases
└── README.md         # This file
```

## Edge Cases to Consider

### For `factorial(n)`:

- n = 0 (should return 1)
- n = 1 (should return 1)
- Negative numbers (should raise ValueError)
- Large numbers (consider performance)

### For `fibonacci(n)`:

- n = 0 (should return 0)
- n = 1 (should return 1)
- Negative numbers (should raise ValueError)
- Large numbers (consider performance and algorithm efficiency)

### For `fizzbuzz(n)`:

- n = 0 (should return empty list)
- n = 1 (should return [1])
- Negative numbers (should raise ValueError)
- Large numbers (memory considerations)

## Testing Guidelines

- Test normal cases and edge cases
- Test error conditions (like non-string input for `count_unique`)
- Use descriptive test method names
- Include comments explaining complex test scenarios
- Aim for high test coverage

## Example Test Structure

```python
import unittest
from main import factorial, fibonacci, fizzbuzz

class TestAlgorithmFunctions(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        pass
    
    def tearDown(self):
        """Clean up after each test method."""
        pass
    
    # Test cases for each function...
    
if __name__ == "__main__":
    unittest.main()
```