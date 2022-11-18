
# You are given an array of integers prices where prices[i] is the price of a given stock on the ith day.
# You can only sell after you buy the stock.
# You have to find the maximum profit that you can make by buying and selling the stock.


# Tags: Dynamic Programming, Array


# Problem Statement 1: Find the maximum profit. You can only do one transaction, i.e., buy the stock and sell it once.

# Approach:
# Calculate the cummulative difference array. Find the maximum sum subarray in it using Kadane.

# Algorithm:
# 1. Initialize max_profit = 0, curr_profit = 0.
# 2. Iterate over the array from 1 to n - 1, and do the following:
#   a. Set current as prices[i] - prices[i - 1].
#   b. Set curr_profit as max(curr_profit + current, current).
#   c. Set max_profit as max(max_profit, curr_profit).
# 3. Return max_profit.

# Time Complexity: O(n)
# Space Complexity: O(1)

def max_profit_single_transaction(prices):

    n=len(prices)
    max_profit = 0
    curr_profit = 0

    for i in range(1, n):
        current = prices[i] - prices[i - 1]
        curr_profit = max(curr_profit + current, current)
        max_profit = max(max_profit, curr_profit)

    return max_profit



# <-- End of Problem Statement 1 -->


# Problem Statement 2: Find the maximum profit. You can do as many transactions as you want, i.e., buy the stock and sell it multiple times.
# You can only hold one stock at a time.

# Approach:
# Summation of all positive cummulative differences.

# Algorithm:
# 1. Initialize max_profit = 0.
# 2. Iterate over the array from 1 to n - 1, and do the following:
#   a. Set current as prices[i] - prices[i - 1].
#   b. If current > 0, then add current to max_profit.
# 3. Return max_profit.


def max_profit_multiple_transactions(prices):

    n=len(prices)
    max_profit = 0

    for i in range(1, n):
        current = prices[i] - prices[i - 1]
        if current > 0:
            max_profit += current

    return max_profit


# <-- End of Problem Statement 2 -->

