

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