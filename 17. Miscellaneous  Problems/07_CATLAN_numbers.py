
# CATLAN numbers is a sequence of natural numbers defined by the following
# recurrence relation:
#   C(0) = 1
#   C(n+1) = sum(C(i)*C(n-i)) for i=0 to n  (n>=0)
#
# The first few terms of the sequence are:
# C(0) = 1
# C(1) = 1
# C(2) = C(0)*C(1) + C(1)*C(0) = 2
# C(3) = C(0)*C(2) + C(1)*C(1) + C(2)*C(0) = 5

# Time Complexity: O(n^2)
# Space Complexity: O(n)


dp=[0]*100

def catlan(n:int) ->int:

    if n==0 or n==1:
        return 1

    if dp[n]!=0:
        return dp[n]

    for i in range(n):
        dp[n]+=catlan(i)*catlan(n-i-1)

    return dp[n]        






# Application of CATLAN numbers:
# 1. Number of BSTs with n nodes
# 2. Number of full binary trees with n+1 leaves
# 3. Number of expressions containing n pairs of parentheses which are correctly matched
# 4. Number of ways n+1 factors can be completely parenthesized
# 5. Number of ways n points can be connected by n-1 line segments without self intersection
# 6. Number of non-isomorphic binary trees with n nodes
# 7. Number of ways n+1 vertices can be connected by n edges without forming a cycle


