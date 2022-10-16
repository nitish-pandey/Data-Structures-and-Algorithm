
# AVL tree is a self-balancing Binary Search Tree (BST) where the difference between heights of left and right subtrees cannot be more than one for all nodes.

# Advantages of AVL Tree over BST:
#   1. AVL trees provide faster lookups than BST because they are more balanced compared to BSTs.
#   2. AVL trees provide faster insertion and deletion operations than BST because they are more balanced compared to BSTs.

# Disadvantages of AVL Tree over BST:
#   1. AVL trees require more memory than BSTs because they store balance factors with each node.
#   2. AVL trees are slower than Red-Black Trees because they may require one or two tree rotations during insertion and deletion.





class AVL:

    class node:

        def __init__(self,data=0) -> None:
            self.data=data
            self.left=None
            self.right=None
            self.height=1
            pass
    
    def __init__(self) -> None:
        self.__root=None
        pass

    def insert(self,a):
        self.__root=self.__insert(self.__root,a)
        return
    
    def __insert(self,root,a):
        if root==None:
            return self.node(a)
        
        if root.data>a:
            root.left=self.__insert(root.left,a)
        else:
            root.right=self.__insert(root.right,a)
        
        root.height=1+max(self.__height(root.left),self.__height(root.right))
        
        balance=self.__get_balance(root)
        
        if balance>1 and a<root.left.data:
            return self.__right_rotate(root)
        
        if balance<-1 and a>root.right.data:
            return self.__left_rotate(root)
        
        if balance>1 and a>root.left.data:
            root.left=self.__left_rotate(root.left)
            return self.__right_rotate(root)
        
        if balance<-1 and a<root.right.data:
            root.right=self.__right_rotate(root.right)
            return self.__left_rotate(root)
        
        return root
    
    def __height(self,root):
        if root==None:
            return 0
        return root.height
    
    def __get_balance(self,root):
        if root==None:
            return 0
        return self.__height(root.left)-self.__height(root.right)
    
    def __right_rotate(self,z):
        y=z.left
        T3=y.right
        
        y.right=z
        z.left=T3
        
        z.height=1+max(self.__height(z.left),self.__height(z.right))
        y.height=1+max(self.__height(y.left),self.__height(y.right))
        
        return y
    
    def __left_rotate(self,z):
        y=z.right
        T2=y.left
        
        y.left=z
        z.right=T2
        
        z.height=1+max(self.__height(z.left),self.__height(z.right))
        y.height=1+max(self.__height(y.left),self.__height(y.right))
        
        return y
    
    def preorder(self):
        self.__preorder(self.__root)
        return

    def __preorder(self,root):
        if root==None:
            return
        print(root.data,end=" ")
        self.__preorder(root.left)
        self.__preorder(root.right)
        return
    
    def inorder(self):
        self.__inorder(self.__root)
        return
    
    def __inorder(self,root):
        if root==None:
            return
        self.__inorder(root.left)
        print(root.data,end=" ")
        self.__inorder(root.right)
        return
    
    def postorder(self):
        self.__postorder(self.__root)
        return
    
    def __postorder(self,root):
        if root==None:
            return
        self.__postorder(root.left)
        self.__postorder(root.right)
        print(root.data,end=" ")
        return
    
    def levelorder(self):
        self.__levelorder(self.__root)
        return
    
    def __levelorder(self,root):
        if root==None:
            return
        q=[]
        q.append(root)
        while len(q)>0:
            a=q.pop(0)
            print(a.data,end=" ")
            if a.left:
                q.append(a.left)
            if a.right:
                q.append(a.right)
        return
    
    def search(self,a):
        return self.__search(self.__root,a)
    
    def __search(self,root,a):
        if root==None:
            return False
        if root.data==a:
            return True
        if root.data>a:
            return self.__search(root.left,a)
        return self.__search(root.right,a)

    
# Explain Insertion in AVL tree

# 1. Perform the normal BST insertion.
# 2. Get the balance factor of the current node (root).
# 3. If balance factor is greater than 1, then the current node is unbalanced and we are either in Left Left case or Left Right case. To check whether it is Left Left case or Left Right case, compare data with root’s left child’s data.
# 4. If balance factor is less than -1, then the current node is unbalanced and we are either in Right Right case or Right Left case. To check whether it is Right Right case or Right Left case, compare data with root’s right child’s data.
