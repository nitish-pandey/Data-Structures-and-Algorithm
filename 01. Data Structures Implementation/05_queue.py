
# Queue is a linear data structure which follows a particular order in which the operations are performed. 
# The order is First In First Out (FIFO). 
# A good example of queue is any queue of consumers for a resource where the consumer that came first is served first. 
# The difference between stacks and queues is in removing. In a stack we remove the item the most recently added; in a queue, we remove the item the least recently added.


# Advantages:
# 1. Easy to implement. It can be easily implemented using array or linked list.
# 2. It allows a fast access to any element in the queue.
# 3. It is useful where data is transferred asynchronously (data not necessarily received at same rate as sent) between two processes. For example, IO Buffers, pipes, file IO, etc.


# Disadvantages:
# The priority of the elements is not taken into account while processing.
# The data can not be accessed randomly. It has to be accessed sequentially starting from the first element.


class queue:
    class __node:

        def __init__(self,data) -> None:
            self.data=data
            self.next=None
            pass

    def __init__(self) -> None:
        self.__front=None
        self.__back=None
        pass

    def insert(self,a):
        temp=self.__node(a)

        if self.__front==None:
            self.__front=temp
            self.__back=temp
            return

        self.__back.next=temp
        self.__back=temp
        return

    def top(self):
        if self.__front:
            return self.__front.data
        return -1
        
    def delete(self):
        if self.__front==None:
            return
        
        self.__front=self.__front.next
        return

    def traverse(self):
        temp=self.__front
        if temp==None:
            print("Queue is empty.")
            return

        print("The queue is : ")
        while temp:
            print(temp.data,end="-> ")
            temp=temp.next
        print()





# Dequeue is an extension of queue with following properties.

# 1. Elements can be inserted and deleted at both ends.
# 2. Either of the end works as front and rear.
# 3. The queue that supports both insertion and deletion at both ends is called ‘Double Ended Queue’ or ‘Deque’ for short.


# Advantages:
# 1. It can be used as both queue and stack.
# 2. It can be used to implement both FIFO and LIFO.
# 3. It can be used to implement priority queue.


class deque:

    class __node:

        def __init__(self,data) -> None:
            self.data=data
            self.next=None
            self.prev=None
            pass
    

    def __init__(self) -> None:
        self.__front=None
        self.__back=None
        pass


    def insert_front(self,a):
        temp=self.__node(a)

        if self.__front==None:
            self.__front=temp
            self.__back=temp
            return

        temp.next=self.__front
        self.__front.prev=temp
        self.__front=temp
        return

    
    def insert_back(self,a):
        temp=self.__node(a)

        if self.__front==None:
            self.__front=temp
            self.__back=temp
            return

        self.__back.next=temp
        temp.prev=self.__back
        self.__back=temp
        return

    
    def delete_front(self):
        if self.__front==None:
            return

        self.__front=self.__front.next
        return

    
    def delete_back(self):

        if self.__front==None:
            return

        self.__back=self.__back.prev
        return

    
    def traverse(self):
        temp=self.__front
        if temp==None:
            print("Queue is empty.")
            return

        print("The queue is : ")
        while temp:
            print(temp.data,end="-> ")
            temp=temp.next
        print()


    def top(self):

        if self.__front:
            return self.__front.data
        return -1

    def back(self):
        if self.__back:
            return self.__back.data
        return -1

    def size(self):
        temp=self.__front
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count

