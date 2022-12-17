

class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev=None



# Class: Stack

# Operations:
# 1. Push : insert the element at the top
# 2. Pop: remove the element from the top
# 3. Peek: See the top element of stack
# 4. isEmpty: Check if Empty


class stack:

    def __init__(self) -> None:
        self.root==None
        pass

    def push(self,a):
        temp=node(a)

        temp.next=self.root
        self.root=temp

        return

    
    def pop(self):
        if self.root==None:
            return -1

        a=self.root.data

        self.root=self.root.next

        return

    
    def peek(self):

        if self.root==None:
            return -1

        return self.root.data


    def isEmpty(self):

        return self.root==None

    

# Class: Queue

# Operations:
# 1. Enqueue: Insert at the bottom
# 2. Dequeue: Remove from the top
# 3. front: return the Front element


class queue:

    def __init__(self) -> None:
        self.head=None
        self.tail=None
        pass

    def enqueue(self,data):
        temp=node(data)

        if self.head==None:
            self.head=self.tail=temp
            return

        self.tail.next=temp
        self.tail=temp

        return

    
    def dequeue(self):
        if self.head==None:
            return -1

        temp=self.head.data

        self.head=self.head.next

        return temp

    
    def front(self):

        if self.head:
            return self.head.data

        return -1


    
    def isEmpty(self):

        return self.head==None

        

# Class: Dequeue

# Operations:
# 1. Push front
# 2. Push Back
# 3. Pop front
# 4. Pop back
# 5. Front
# 6. Back



class dequeue:

    def __init__(self) -> None:
        self.head=None
        self.tail=None
        pass


    def push_front(self,data):
        temp=node(data)

        if self.head==None:
            self.head=self.tail=temp
            return

        temp.next=self.head
        self.head=temp

        return        

    def push_back(self,data):
        temp=node(data)

        if self.head==None:
            self.head=self.tail=temp
            return

        self.tail.next=temp
        temp.prev=self.tail
        self.tail=temp

        return

    
    def pop_front(self):
        if self.head==None:
            return -1

        temp=self.head.data

        self.head=self.head.next
        self.head.prev=None

        return temp

    def pop_back(self):
        if self.head==None:
            return -1

        temp=self.back.data

        self.back=self.head.prev
        self.back.next=None

        return temp

    
    def front(self):

        if self.head:
            return self.head.data

        return -1

    def back(self):

        if self.tail:
            return self.tail.data

        return -1

    
    def isEmpty(self):

        return self.head==None

        