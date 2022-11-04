
# Problem Statement: Find the GCD of two numbers
# GCD of two numbers is the largest number that divides both of them.

# For example GCD of 20 and 28 is 4 and GCD of 98 and 56 is 14

# Solution: Euclidean Algorithm

# Algorithm:
# 1. If any of the number is 0 then return the other number
# 2. Return the recursive call of the function with the smaller number and the remainder of the larger number divided by the smaller number

# Time Complexity: O(log(min(a,b)))
# Space Complexity: O(log(min(a,b)))

def gcd(a, b):

    if b==0:
        return a
    
    return gcd(b, a%b)




