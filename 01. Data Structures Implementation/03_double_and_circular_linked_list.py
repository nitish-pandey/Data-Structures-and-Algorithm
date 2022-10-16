# Doubly linked list is a linked list where each node has two pointers, one to the next node and one to the previous node.

# Advantages:
# 1. It can be traversed in both forward and backward direction.
# 2. The delete operation in DLL is more efficient if pointer to the node to be deleted is given.
# 3. We can quickly insert a new node before a given node.

# Disadvantages:
# 1. Every node of DLL Require extra space for an previous pointer. It is possible to implement DLL with single pointer though (See this and this).
# 2. All operations require an extra pointer previous to be maintained. For example, in insertion, 
#       we need to modify previous pointers together with next pointers. For example in following functions
#       for insertions at different positions, we need 1 or 2 extra steps to set previous pointer.




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



# Circular linked list is a linked list where all nodes are connected to form a circle.

# Advantages:
# 1. Any node can be a starting point. We can traverse the whole list by starting from any point. We just need to stop when the first visited node is visited again.
# 2. Useful for implementation of queue. Unlike simple linked list, we don’t need to maintain two pointers for front and rear if we use circular linked list. We can maintain a pointer to the last inserted node and front can always be obtained as next of last.


# Disadvantages:
# 1. Each node of circular linked list must store two pointers (for previous and next). For singly linked list, circular linked list requires extra space for an address pointer.
# 2. Nodes cannot be easily removed from a circular linked list.



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


