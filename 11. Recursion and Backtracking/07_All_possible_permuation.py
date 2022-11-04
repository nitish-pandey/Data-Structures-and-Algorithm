
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

        if i>0 and s[i]==s[i-1]:
            continue

        solve_string(s[:i]+s[i+1:],curr+s[i])




def permute_string(s):

    s=''.join(sorted(s))
    print(s)
    
    solve_string(s,"")

    return ans




# Problem Statement: You are given a array of size N, return all the possible permuations of array


