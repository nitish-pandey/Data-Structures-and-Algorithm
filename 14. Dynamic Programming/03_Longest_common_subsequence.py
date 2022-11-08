
# Problem Statement:    Given two sequences, find the length of longest subsequence present in both of them. 
#                       A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
#                       For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”. 
#                       So a string of length n has 2^n different possible subsequences.



# Algorithm:

# 1. Create a 2D array of size (m+1) x (n+1)
# 2. Initialize the first row and first column with 0
# 3. Iterate from 1 to m
# 4. Iterate from 1 to n
# 5. If str1[i-1] == str2[j-1], then dp[i][j] = 1 + dp[i-1][j-1]
# 6. Else, dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# 7. Return dp[m][n]


# Time Complexity: O(mn)
# Space Complexity: O(mn)


# Dynamic Programming Solution

def lcs_dp(str1, str2):

    m = len(str1)
    n = len(str2)

    dp = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]



def main():

    str1 = "AGGTAB"
    str2 = "GXTXAYB"

    print(lcs_dp(str1, str2))



main() # Call to main()

# Output:
# 4

# Explanation:
# The longest common subsequence is "GTAB" which has length 4
