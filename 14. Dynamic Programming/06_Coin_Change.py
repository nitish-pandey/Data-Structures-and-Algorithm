

# Problem Statement 1: You are given a array of coins and a target amount. You have to return the minimum number of coins required to make the target amount.
# You can use any number of coins of any denomination. (i.e. infinite supply of coins)

# Tags: Dynamic Programming, Coin Change

# Approach: We will use dynamic programming to solve this problem.


# Algorithm:
# 1. We will create a dp array of size target+1 and initialize it with infinity. ( or -1 as per our choice)
# 2. We will iterate over the dp array and for each index we will iterate over the coins array ()
# 3. Check if the current coin is less than or equal to the target amount, if no then continue
# 4. We will update the dp[curr] with minimum of dp[curr] and dp[curr-coin]+1
# 5. We will return dp[target] if dp[target] is not infinity else we will return -1

# Time Complexity: O(n*m)
# Space Complexity: O(n)


def coin_change(coins:list,target:int) ->int:

    n=len(coins)

    dp=[100000 for i in range(target+1)]

    dp[0]=0

    for i in range(target+1):

        for coin in coins:

            curr=i+coin

            if curr>target:

                continue

            dp[curr]=min(dp[curr],dp[i]+1)

    
    if dp[target]==100000:

        return -1

    return dp[target]





# Problem Statement 2: Same Problem but limited supply of coins ( each coin can be used only once)

# Tags: Dynamic Programming, Coin Change



coins=[4,5,2]

print(coin_change(coins,11))