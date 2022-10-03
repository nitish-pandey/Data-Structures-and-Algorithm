
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

    
