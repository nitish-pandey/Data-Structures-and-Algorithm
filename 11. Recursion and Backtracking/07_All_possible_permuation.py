
# Problem Statement: You are given a string S, you have to return all the possible permutation of a string in lexographically sorted array

# Tags: Recursion, String, Permutation, Backtracking

# Approach: We will use backtracking to solve this problem.
# We have to sort the string first in order to get in lexographically sorted array
# We will create a curr string and append the character to it and call the function recursively
# We will also check if the character is already present in the curr string or not, if it is present then we will not append it to the curr string to avoid duplicates


# Algorithm:
# We will use backtracking to solve this problem. 
# We will check if the length of the string is 0, if yes then we will append the current string to the answer list and return.
# We will iterate over the string and check if the current character is equal to the previous character, if yes then we will continue.
# We will call the solve function with the string without the current character and the current character appended to the current string.
# We will return the answer list.

# Time Complexity: O(n*n!)
# Space Complexity: O(n*n!)

ans=[]

def solve_string(s,curr):

    if len(s)==0:

        ans.append(curr)

        return

    for i in range(len(s)):

        if i>0 and s[i]==s[i-1]:  # to avoid duplicates
            continue

        solve_string(s[:i]+s[i+1:],curr+s[i])




def permute_string(s):

    s=''.join(sorted(s))

    ans.clear()  

    solve_string(s,"")

    return ans




# Problem Statement: You are given a array of size N, return all the possible permuations of array

# Approach: 
#  We will take the call the recursive function with the array and the index 0
# From the given index upto last, we will swap the current index with the other index and call the function recursively,
# After the recursive call, we will swap the current index with the other index to get the original array


# Algorithm:
# 1. Base Case: If the index is equal to the length of the array, then we will append the array to the answer list and return
# 2. We will iterate over the array from the given index to the last index
# 3. We will check if element at the current index is equal to the element at the previous index, if yes then we will continue
# 4. We will swap the current index with the other index and call the function recursively
# 5. After the recursive call, we will swap the current index with the other index to get the original array



all_permutations=[]


def solve_array(arr:list,ind:int):

    if ind==len(arr):

        all_permutations.append(arr)

        return

    for i in range(ind,len(arr)):
        
        if ind!=i and arr[ind]==arr[i]: # to avoid duplicates
            continue

        arr[ind],arr[i]=arr[i],arr[ind]

        solve_array(arr,ind+1)

        arr[ind],arr[i]=arr[i],arr[ind]




def permute_array(arr:list) -> list:

    all_permutations.clear()

    solve_array(arr,0)

    return all_permutations



def main():

    string="aab"
    arr=[1,2,2]

    print("The permutations of string are: \n",permute_string(string))
    print("\nThe permutations of array are: \n",permute_array(arr))


main()


# Output:

#  The permutations of string are: 
#  ['aab', 'aba', 'baa']

#  The permutations of array are: 
#  [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]