
# Problem Statement: You have to find the nth fibonacci number

# Fibonacci series is the series in which each number is the sum of the previous two numbers.

# Tags: Recursion, Fibonacci


# Algorithm:
# 1. If n is less than 2, return n as it is  (base case)
# 2. Call the function recursively for n-1 and n-2
# 3. Return the sum of the two numbers

# Time Complexity: O(2^n)
# Space Complexity: O(n)

def fib(n):

    if n<2:
        return n

    return fib(n-1)+fib(n-2)




# Problem Statement: You have to find the factorial of a number

# Factorial of a number is the product of all the numbers from 1 to that number

# Tags: Recursion, Factorial

# Algorithm:
# 1. If n is less than 3, return n as it is  (base case)
# 2. Call the function recursively for n-1
# 3. Return the product of the ans and n


# Time Complexity: O(n)
# Space Complexity: O(n)

def fact(n):

    if n<3:
        return n

    return n*fact(n-1)


