
# You are given a number N. You need to check if the number is a palindrome or not.

# A palindrome is a number which is same after reverse.


# Algorithm for reversing a number:
# 1. Initialize a variable rev=0
# 2. Iterate till n>0:
# 3. rev=rev*10+n%10
# 4. n=n//10
# 5. Return rev


# Algorithm:
# 1. Reverse the number
# 2. Compare the reversed number with the original number
# 3. If both are same, then the number is a palindrome


# Time Complexity: O(logn)
# Space Complexity: O(1)


def isPalindrome(n):

    def reverse(n):

        rev=0

        while n>0:

            rev=rev*10+n%10
            n=n//10

        return rev


    return n==reverse(n)



