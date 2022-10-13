
# Problem Statement: Find the nth number of fibonacci series


dp=[0]*1000 

def fibonacci(n):

    if n<=2:
        return 1

    if dp[n]:
        return dp[n]


    dp[n]= fibonacci(n-1)+fibonacci(n-2)

    return dp[n]



def main():

    n=235

    print(fibonacci(n))


main()



    