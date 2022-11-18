
# Problem Statement: You are given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n.
# Determine the maximum value obtainable by cutting up the rod and selling the pieces.

# Tags: Dynamic Programming

# Input: 8
#        1 5 8 9 10 17 17 20

# Output: 22

# Explanation: The maximum obtainable value is 22 by cutting in two pieces of lengths 2 and 6


# Algorithm:
# 1. Create an array of size n + 1 and initialize it with 0.
# 2. Iterate over the array from 1 to n, and do the following:
#    a. Iterate over the array from 0 to i - 1, and do the following:
#       i. Update the value of dp[i] as max(dp[i], price[j] + dp[i - j - 1]).
# 3. Return dp[n].

# Time Complexity: O(n^2)
# Space Complexity: O(n)


def rod_cutting(length, price):

    dp = [0] * (length + 1)

    for i in range(1, length + 1):
        for j in range(i):
            dp[i] = max(dp[i], price[j] + dp[i - j - 1])

    return dp[length]



