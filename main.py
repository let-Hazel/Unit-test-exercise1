# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         if n < 0:
#             return "input positive number"
#         if n == 0:
#             return 1
#         else:
#             fact *= i
#     return fact

# # print(factorial(3))

def fibonacci(n):
    """
    fn = f(n-1)+ f(n-2)
    """
    if not n.isdigit():
        raise ValueError or NameError
    if n < 0:
        return "only positive integers"
    elif n == 1:
        return "only numbers above 1"
    else:
        seq = [0,1]
        for i in range(2,n+1):
            num = seq[i-1] + seq[i-2]
            seq.append(num)
            nth = seq[-1]

    return nth, seq

print(fibonacci("p"))
    

# def fizzbuzz(n):
#     result = []
#     for i in range(1, n+1):  
#     # while n <= n:  
#         if i%3==0 and i%5==0:
#             result.append("FizzBuzz")

#         elif i%3==0:
#            result.append("Fizz")

#         elif i%5==0:
#             result.append("Buzz")
            
#         else:
#             result.append(i) 

#     return result

#     # return i
# # fizzbuzz(3)
# # print(fizzbuzz(15))



