

from bst import *

# Problem Statement: You are given a Binary Tree. Return the largest  binary search tree.


def isValidBST(root:node) -> bool:
    if not root:
        return True

    if not root.left and not root.right:
        return True


    def maximum(root:node):
        if not root.right:
            return root.data

        return maximum(root.right)


    def minimum(root:node):
        if not root.left:
            return root.data

        return minimum(root.left)


    if root.left and maximum(root.left)>=root.data:
        return False


    if root.right and minimum(root.right)<=root.data:
        return False

    return isValidBST(root.left) and isValidBST(root.right)



def size(root:node):
    if not root:
        return 0

    return size(root.left)+size(root.right)+1


def maxBST(root:node):
    if not root or (not root.left and not root.right):
        return root

    if isValidBST(root):
        return root

    l=maxBST(root.left)
    r=maxBST(root.right)

    if size(l)>size(r):
        return l

    return r





def main():

    tree=BST()

    tree.insert(4)
    tree.insert(6)
    tree.insert(3)
    tree.insert(9)
    tree.insert(5)
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)

    temp=node(10)
    temp.right=tree.root
    

    ans=maxBST(temp)

    print(size(ans))


main()



    