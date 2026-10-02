def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)

print(factorial(5))
print( factorial(0), factorial(1))

def factorial(n, depth = 0):
    pad = " " * depth
    print(f"{pad} factorial {n} called")
    if n <= 1:
        print(f"{pad}-> base case returns 1")
        return 1
    result = n * factorial(n - 1, depth + 1)
    print(f"{pad} -> returns {result}")
    return result

factorial(4)

def countdown(n):
    print(n)
    countdown(n - 1)

countdown(3)

def countdown(n):
    if n <= 0:
        print("liftoff:")
        return
    print(n)
    countdown(n - 1)

countdown(3)

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n-2)

for i in range(8):
    print(fib(i), end = " ")

def factorial_loop(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_rec(n):
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)

print(factorial_loop(5), factorial_rec(5))  # this prints 120 120. Both functions calculate 5 factorial (5 x 4 x 3 x 2 x 1), so they give the same answer. factorial_loop multiplies the numbers from 2 up to n using a for loop, while factorial_rec calls itself with n - 1 until it reaches the base case n <= 1. The loop version is simpler and uses less memory, but the recursive one matches the maths definition more closely
