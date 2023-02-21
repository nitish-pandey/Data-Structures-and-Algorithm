
# Problem Statement: You are given 2 numbers a and b. You need to find the GCD of those 2 numbers.

# GCD (Greatest Common Divisor) of 2 numbers is the largest number that divides both of them.
# It is also known as HCF (Highest Common Factor) of 2 numbers.


# Tags: Maths, GCD, HCF

# Approach 1: Euclidean Algorithm

# Algorithm:
# 1. If b is 0, return a
# 2. Else return gcd(b,a%b)


# Time Complexity: O(log(min(a,b)))
# Space Complexity: O(1)

def gcd(a:int,b:int) -> int:
    if(b==0):
        return a
    else:
        return gcd(b,a%b)


    