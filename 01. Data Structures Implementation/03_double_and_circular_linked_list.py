
class double_linked_list:

    class __node:
        def __init__(self,data=0) -> None:
            self.data=data
            self.next=None
            self.prev=None
            pass
    
    def __init__(self) -> None:
        self.root=None
        pass

    def insert(self,a):
        temp=self.__node(a)

        if self.root:
            self.root.prev=temp
        
        temp.next=self.root

        self.root=temp
        return

    def delete(self):
        if self.root==None:
            return
        
        self.root=self.root.next

        if self.root:
            self.root.prev=None
        return

    def traverse(self):

        temp=self.root
        if temp==None:
            print("Linked list is empty.")
            return

        print("The linked list is : ")
        while temp:
            print(temp.data,end=", ")
            temp=temp.next
        print()




class circular_linked_list:

    class __node:
        def __init__(self,data=0) -> None:
            self.data=data
            self.next=None
            pass
    
    def __init__(self):
        self.root=None
        pass

    def insert(self,a):
        temp=self.__node(a)

        if self.root==None:
            self.root=temp
            temp.next=temp
            return

        ptr=self.root

        while ptr.next!=self.root:
            ptr=ptr.next
        
        ptr.next=temp
        temp.next=self.root
        return

    def delete(self):
        if self.root==None:
            return
        
        if self.root.next==self.root:
            self.root=None
            return

        ptr=self.root

        while ptr.next!=self.root:
            ptr=ptr.next
        
        ptr.next=self.root.next
        self.root=self.root.next
        return

    def traverse(self):

        temp=self.root
        if temp==None:
            print("Linked list is empty.")
            return

        print("The linked list is : ")
        while temp.next!=self.root:
            print(temp.data,end=", ")
            temp=temp.next
        print(temp.data)
        return



class double_circular_linked_list:

    class __node:
        def __init__(self,data=0) -> None:
            self.data=data
            self.next=None
            self.prev=None
            pass
    
    def __init__(self) -> None:
        self.root=None
        pass

    def insert(self,a):
        temp=self.__node(a)

        if self.root==None:
            self.root=temp
            temp.next=temp
            temp.prev=temp
            return

        ptr=self.root

        while ptr.next!=self.root:
            ptr=ptr.next
        
        ptr.next=temp
        temp.prev=ptr
        temp.next=self.root
        self.root.prev=temp
        return

    def delete(self):
        if self.root==None:
            return
        
        if self.root.next==self.root:
            self.root=None
            return

        ptr=self.root

        while ptr.next!=self.root:
            ptr=ptr.next
        
        ptr.next=self.root.next
        self.root=self.root.next
        self.root.prev=ptr
        return

    def traverse(self):

        temp=self.root
        if temp==None:
            print("Linked list is empty.")
            return

        print("The linked list is : ")
        while temp.next!=self.root:
            print(temp.data,end=", ")
            temp=temp.next
        print(temp.data)
        return


