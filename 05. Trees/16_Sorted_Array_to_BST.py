from bst import *



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