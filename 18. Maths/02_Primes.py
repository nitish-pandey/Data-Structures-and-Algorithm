

# Problem Statement: Find Out the Prime numbers till n


# Approach 1

# 1. Iterate from 2 to n
# 2. Check for Prime, if yes print i


# Check for Prime
# Iterate from i=2 to i*i <= n
# if n is divisible by i, return False
# At the last return True

# Time Complexity: O(sqrt(n))

def isPrime(n):
    i=2

    while i*i<=n:

        if n%i==0:
            return False
        
    return True


# Time Complexity: O(n*sqrt(n))
# Space Complexity: O(1)

def print_primes(n):

    for i in range(2,n+1):

        if isPrime(i):
            print(i,end=' ')

    return




# Approach 2: Seive of Erasthothenis


# 1. Create a array-prime of size n+1 and initialize True to all
# 2. Iterate from 2 to N:
# 3. If the current number is prime, then mark its all multiples from its square upto n as non-prime
# 4. Iterate from 2 to N, if it is prime print it.


# Time Complexity: O(n*log(logn))
# Space Complexity: O(n)


def seive_of_erasthothenis(n):

    if n<2:
        return 

    prime=[True]*(n+1)

    for i in range(2,n+1):

        if prime[i]:

            for j in range(i*i,n+1,i):
                prime[j]=False

    
    for i in range(2,n+1):

        if prime[i]:
            print(i,end=" ")

    print()



