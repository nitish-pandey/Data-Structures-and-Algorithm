
# Given a Bucket having a capacity of N litres and the task is to determine that by how many ways you can fill it using two bottles of capacity of 1 Litre and 2 Litre only. Find the answer modulo 108.

# Input:
# 3
# Output:
# 3 


# Input:
# 4
# Output:
# 5 


def bucket_filling(N):

    dp=[0]*(N+1)

    for i in range(2,N+1):
        dp[i]=dp[i-2]+2

    