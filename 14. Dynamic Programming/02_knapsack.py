

# Problem Statement:    Given weights and values of n items, put these items in a knapsack 
#                       of capacity W to get the maximum total value in the knapsack. In other words, 
#                       given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively.
#                       Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that
#                       sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item,
#                       or don’t pick it (0-1 property).



# Algorithm:

# 1. Create a 2D array of size (n+1) x (W+1)
# 2. Initialize the first row and first column with 0
# 3. Iterate from 1 to n
# 4. Iterate from 1 to W
# 5. If wt[i-1] <= j, then dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
# 6. Else, dp[i][j] = dp[i-1][j]
# 7. Return dp[n][W]


# Time Complexity: O(n * W)
# Space Complexity: O(n * W)



# Dynamic Programming Solution

def knapsack_dp(val, wt, W):

    n = len(val)

    dp = [[0 for i in range(W+1)] for j in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, W+1):
            if wt[i-1] <= j:
                dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][W]




