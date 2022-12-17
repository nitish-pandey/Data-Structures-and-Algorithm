
# Problem Statement: You are given inorder and preorder traversals of a binary tree in the form of arrays.
# Create a binary tree from these traversals.

# Input: Inorder traversal: [4, 2, 5, 1, 6, 3, 7]
#        Preorder traversal: [1, 2, 4, 5, 3, 6, 7]

# Output: Binary tree:
#             1
#           /   \
#          2     3
#         / \   / \
#        4   5 6   7



# Algorithm:
# 1. Pick element at indx from preorder and create a node
# 2. Increament the indx
# 3. Search for the element at the inorder as position pos
# 4.  Call the function from (start to pos-1) for left child of Tree
# 5.  Call the function from (pos+1 to end) for right child of Tree

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

def create_tree(preorder,inorder,start,end):

    global indx

    if indx>=len(preorder) or start>end:
        return None

    temp_data=preorder[indx]
    indx+=1

    temp_node=node(temp_data)

    pos=search(inorder,start,end,temp_data)

    if pos==-1:
        return temp_node

    temp_node.left=create_tree(preorder,inorder,start,pos-1)
    temp_node.right=create_tree(preorder,inorder,pos+1,end)

    return temp_node




    

    
# Post Order Traversal
def postorder(root:node) :

    if root==None:
        return

    postorder(root.left)
    postorder(root.right)

    print(root.data,end=" ")




def main():

    Inorder =[4, 2, 5, 1, 6, 3, 7]
    Preorder = [1, 2, 4, 5, 3, 6, 7]

    tree=create_tree(Preorder,Inorder,0,len(Inorder)-1)

    postorder(tree)


main() # calling main function

# Output:
# 4 5 2 6 7 3 1