from bst import *

# Problem Statement: You are given an sorted array, convert it into the balanced BST


# Algorithm:
# 1. If start>end: return NULL
# 2. Find out the mid element and create the curr node 
# 3. call the function recursively from start to mid-1 and store it in left of the curr
# 4. call the function recursively from mid+1 to end and store it in right of the curr
# 5. Return the curr node

# Time Complexity: O(n)
# Space Complexity: O(log n )

def arr_to_bst(arr:list(),st:int,end:int) ->node:

    if st>end:
        return None

    mid=(st+end)//2

    temp=node(arr[mid])

    temp.left=arr_to_bst(arr,st,mid-1)
    temp.right=arr_to_bst(arr,mid+1,end)

    return temp





def inorder(root:node):

    if not root:
        return

    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)



def main():

    arr=[1,2,3,4,5,6,7,8,9,99]

    root=arr_to_bst(arr,0,len(arr)-1)
    inorder(root)



main()  # call to main function

# Output:
# 1 2 3 4 5 6 7 8 9 99 
