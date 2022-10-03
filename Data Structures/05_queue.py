

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

