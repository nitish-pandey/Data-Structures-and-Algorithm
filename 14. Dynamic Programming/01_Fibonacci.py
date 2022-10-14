
# Problem Statement: Find the nth number of fibonacci series using dynamic programming

# Algorithm:
# 1. Create a list of size n+1
# 2. Initialize the first two elements of the list with 0 and 1
# 3. Iterate from 2 to n and update the list with the sum of previous two elements
# 4. Return the nth element of the list

# Time Complexity: O(n)
# Space Complexity: O(n)
 
# Dynamic Programming Solution

def fib_dp(n):
    if n == 0 or n == 1:
        return n

    fib = [0, 1]

    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    
    return fib[n]



def main():

    n = 9

    print(fib_dp(n))


main() # Call to main()


# Output:
# 34




    