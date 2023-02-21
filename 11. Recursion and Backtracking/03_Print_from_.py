
# Problem Statement: Print all the numbers from 1 to n

# Algorithm:
# 1. Base Case: If n<=0, return
# 2. Call same function for n-1
# 3. print(n)

# Time Complexity: O(n)
# Space Complexity: O(n) due to call stack

def print_from_1_to(n):
    if(n<=0):
        return

    print_from_1_to(n-1)
    print(n,end=' ')




    
# Problem Statement: Print all the numbers from n to 1

# Algorithm:
# 1. Base Case: If n<=0, return
# 2. print(n)
# 3. Call same function for n-1

# Time Complexity: O(n)
# Space Complexity: O(n) due to call stack

def print_from_n_to(n):
    if(n<=0):
        return

    print(n,end=' ')
    print_from_n_to(n-1)




    
# Problem Statement: Sum of  all the numbers from n to 1 or 1 to n

# Algorithm:
# 1. Base Case: If n<=0, return 0
# 2. Call the function for n-1 and save the ans
# 3. return ans+ n


# Time Complexity: O(n)
# Space Complexity: O(n) due to call stack

def sum_from_1_to(n):
    if(n<=0):
        return

    ans=sum_from_1_to(n-1)

    return ans+n








    

