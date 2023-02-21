
# Problem Statement: Write a program to check whether a number is Armstrong or not.

# A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.
# abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....

# Example: 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.


# Algorithm:
# 1. Initialize a variable sum=0
# 2. Iterate till n>0:
# 3. sum=sum+pow(n%10,order)
# 4. n=n//10
# 5. Return sum==num


# Time Complexity: O(logn)
# Space Complexity: O(1)


def isArmstrong(num):

    order=len(str(num))

    sum=0

    n=num

    while n>0:

        sum=sum+pow(n%10,order)
        n=n//10

    return sum==num



# Problem Statement: Write a program to check whether a number is perfect or not.
# A positive integer is called a perfect number if sum of all its proper positive divisors excluding the number itself is equal to the number.

# Example: 6 is the first perfect number
# 1, 2, 3 are the proper divisors of 6.
# Sum of proper divisors = 1 + 2 + 3 = 6.


# Algorithm:
# 1. Initialize the variable sum=0
# 2. 