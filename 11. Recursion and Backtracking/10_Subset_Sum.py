
# Problem Statement: You are given a set of numbers and a Sum s. You have to return the subset of the given set so that sum of all elements if s.

# Tags: Backtracking

# Algorithm:
# 1. Check if the sum is less than 0, if yes then return False
# 2. Check if the sum is 0, if yes then return True
# 3. Check if the index is greater than the length of the array, if yes then return False
# 4. Set the value of the index to 1 and check if the subset is found or not for the sum-arr[ind] and index+1
# 5. If the subset is found then return True
# 6. Set the value of the index to 0 and check if the subset is found or not for the sum and index+1
# 7. If the subset is found then return True else return False


# Time Complexity: O(2^n)
# Space Complexity: O(n)


def subset(arr,ans,s,ind):
    if s<0:
        return False
    
    if s==0:
        return True

    if ind>=len(arr):
        return False


    ans[ind]=1
    if subset(arr,ans,s-arr[ind],ind+1):
        return True

    ans[ind]=0
    return subset(arr,ans,s,ind+1)

    


def subset_sum(arr:list,s:int) ->list:

    n=len(arr)

    ans=[0]*n

    if subset(arr,ans,s,0):
        print("Subset found")
        print(ans)
        return 
    print("No subset found")
    return 



# <-- End of Code -->


def main():
    arr=[2,3,5,6,8,10]
    s=12
    subset_sum(arr,s)



main() # call to main function

# Output:
# Subset found
# [1,0,0,0,0,1]


