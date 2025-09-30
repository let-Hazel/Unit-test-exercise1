def factorial(n):
    """Calculates the factorial of a non-negative integer."""
    # TODO: Implement the logic
    for i in range(1, n+1):
        if n < 0:
            return "input positive number"
        if n == 0:
            return 1
 

print(factorial(3))

# def fibonacci(n):
#     """Returns the nth number in the Fibonacci sequence."""
#      x = 0
#      y = 1
#     # TODO: Implement the logic
#     return None

# def fizzbuzz(n):
#     """
#     Returns a list for the FizzBuzz game up to n.
#     - Multiples of 3 are "Fizz"
#     - Multiples of 5 are "Buzz"
#     - Multiples of both 3 and 5 are "FizzBuzz"
#     """
#     # TODO: Implement the logic
#     game = []
#     # for i in range(n):  
#     while n <= n:  
#         if n%3==0 and n%5==0:
#             i = "FizzBuzz"

#         elif n%3==0:
#             i = "Fizz"

#         elif n%5==0:
#             i = "Buzz"
            
#         else:
#             i = n

#     game.append(i)

#     # return i

#     return game
# print(fizzbuzz(2))



