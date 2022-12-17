
# Problem Statement: You are given inorder and preorder traversals of a binary tree in the form of arrays.
# Create a binary tree from these traversals.

# Input: Inorder traversal: [4, 2, 5, 1, 6, 3, 7]
#        Preorder traversal: [4, 5, 2, 6, 7, 3, 1]

# Output: Binary tree:
#             1
#           /   \
#          2     3
#         / \   / \
#        4   5 6   7



# Algorithm:
# 1. Pick element at indx from PostOrder and create a node
# 2. Decreament the indx
# 3. Search for the element at the inorder as position pos
# 4.  Call the function from (pos+1 to end) for right child of Tree
# 5.  Call the function from (start to pos-1) for left child of Tree

# Time Complexity: O(N^2)
# Space Complexity: O(N)


class node:
    def __init__(self,d) -> None:
        self.data=d
        self.left=None
        self.right=None
        pass

def search(arr,st,end,key):
    
    for i in range(st,end+1):
        if arr[i]==key:
            return i

    return -1


# Global or Static Variable
indx=0

def create_tree(postorder,inorder,start,end):

    global indx

    if indx<0 or start>end:
        return None

    temp_data=postorder[indx]
    indx-=1

    temp_node=node(temp_data)

    pos=search(inorder,start,end,temp_data)

    if pos==-1:
        return temp_node
    
    temp_node.right=create_tree(postorder,inorder,pos+1,end)
    temp_node.left=create_tree(postorder,inorder,start,pos-1)

    return temp_node




    

    
# Post Order Traversal
def preorder(root:node) :

    if root==None:
        return
    print(root.data,end=" ")

    preorder(root.left)
    preorder(root.right)





def main():

    Inorder =[4, 2, 5, 1, 6, 3, 7]
    postorder = [4, 5, 2, 6, 7, 3, 1]

    global indx
    indx=len(Inorder)-1

    tree=create_tree(postorder,Inorder,0,len(Inorder)-1)

    preorder(tree)
    print()


main() # calling main function

# Output:
# 1 2 4 5 3 6 7