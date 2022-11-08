

# Problem Statement:    Given weights and values of n items, put these items in a knapsack 
#                       of capacity W to get the maximum total value in the knapsack. In other words, 
#                       given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively.
#                       Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that
#                       sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item,
#                       or don’t pick it (0-1 property).


# Approach 1: Iterative

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


# <-- End of Code -->


# Approach 2: Recursive

# Algorithm:
# 1. Create a 2D array of size (n+1) x (W+1) and initialize it with -1
# 2. If index is equal to n or capacity is equal to 0, then return 0
# 3. If dp[capacity][index] is not equal to -1, then return dp[capacity][index]
# 4. Call the function recursively with index+1 and capacity once selecting the item and once not selecting the item
# 5. store the maximum of the two values in dp[capacity][index]
# 6. Return dp[capacity][index]



def knapSack_Recursive_helper(weights:list,profit:list,capacity:int,dp:list,ind:int) -> int:

    if ind==len(weights) or capacity==0:
        return 0

    if dp[capacity][ind]!=-1:
        return dp[capacity][ind]

    profit1=0

    if weights[ind]<=capacity:
        profit1=profit[ind]+knapSack_Recursive_helper(weights,profit,capacity-weights[ind],dp,ind+1)

    profit2=knapSack_Recursive_helper(weights,profit,capacity,dp,ind+1)

    dp[capacity][ind]=max(profit1,profit2)

    return dp[capacity][ind]






def knapSack_recursive(weights:list,profit:list,capacity:int) ->int:

    n=len(weights)

    if n==0 or capacity==0:
        return 0

    dp=[[-1 for i in range(n)] for j in range(capacity+1)]

    return knapSack_Recursive_helper(weights,profit,capacity,dp,0)
    

def main():

    weights=[1, 3, 4, 5]
    profit=[1, 4, 5, 7]
    capacity=7

    print(knapSack_recursive(weights,profit,capacity))



main()

# Output: 9

# Explanation: The maximum value that can be put in a knapsack of capacity 7 is 9. There are two possible solutions: {1,3,5} and {3,4}.