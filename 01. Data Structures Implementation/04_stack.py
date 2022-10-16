# Stack is a linear data structure which follows a particular order in which the operations are performed.
# The order may be LIFO(Last In First Out) or FILO(First In Last Out).


# Advantages:
# 1. Easy to implement. Memory is not saved as pointers are not involved.
# 2. It can be easily implemented using array or linked list.
# 3. It allows a fast access to any element in the stack.


# Disadvantages:
# 1. It is not dynamic. It doesn't grow and shrink depending on needs at runtime.
# 2. It is not useful where data is constantly being added and removed. For example, in real-time systems where tasks are constantly being scheduled and removed.



class stack:

    class __node:

        def __init__(self) -> None:
            self.data=None
            self.next=None
            pass

    def __init__(self) -> None:
        self.__root=None
        pass

    def push(self,a):
        temp=self.__node()
        temp.data=a
        temp.next=self.__root
        self.__root=temp
        return

    def top(self):
        if self.__root:
            return self.__root.data
        return -1
        
    def pop(self):
        if self.__root==None:
            return
        self.__root=self.__root.next
        return