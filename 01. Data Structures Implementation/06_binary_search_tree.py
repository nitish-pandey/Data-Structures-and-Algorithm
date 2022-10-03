

class BST:

    class __node:
        def __init__(self,a) -> None:
            self.data=a
            self.left=None
            self.right=None
            pass

    def __init__(self) -> None:
        self.__root=None
        pass


    def insert(self,a):

        temp=self.__node(a)

        if self.__root==None:
            self.__root=temp
            return

        ptr=self.__root

        while ptr:

            if ptr.data>a:
                if ptr.left:
                    ptr=ptr.left
                else:
                    ptr.left=temp
                    return
            else:
                if ptr.right:
                    ptr=ptr.right
                else:
                    ptr.right=temp
                    return
        

    def preorder(self):
        
        if self.__root is None:
            return 

        st=[]
        st.append(self.__root)
        print("\nThe pre-order Traversal of BST is : ")

        while len(st)>0:

            a=st.pop()

            print(a.data,end=" ")

            if a.right:
                st.append(a.right)
            if a.left:
                st.append(a.left)

        print()
     
    def inorder(self):
        
        if self.__root is None:
            return 

        st=[]

        curr=self.__root
        print("\nThe in-order Traversal of BST is : ")

        while curr or len(st)>0:

            if curr is not None:
                st.append(curr)
                curr=curr.left
                continue

            curr=st.pop()
            print(curr.data,end=' ')
            curr=curr.right
        print()

    
    def postorder(self):
        
        if self.__root is None:
            return 

        st=[]
        ans=[]
        st.append(self.__root)
        print("\nThe post-order Traversal of BST is : ")

        while len(st)>0:

            a=st.pop()
            ans.append(a.data)
            if a.left:
                st.append(a.left)
            if a.right:
                st.append(a.right)
        
        
        while len(ans)>0:
            print(ans.pop(),end=" ")
            

        print()

        


    def level_order_traversal(self):

        if not self.__root:
            return

        q=[]
        q.append(self.__root)
        print("\nThe level order traversal of BST is : ")

        while len(q)>0:

            a=q.pop(0)
            print(a.data,end=" ")

            if a.left:
                q.append(a.left)
            if a.right:
                q.append(a.right)
        print()
        

    def search(self,a):

        if not self.__root:
            return False

        ptr=self.__root

        while ptr:

            if ptr.data==a:
                return True

            if ptr.data>a:
                ptr=ptr.left
            else:
                ptr=ptr.right
        
        return False