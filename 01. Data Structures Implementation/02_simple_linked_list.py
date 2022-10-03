

class linked_list:

    class __node:
        def __init__(self,data=0) -> None:
            self.data=data
            self.next=None
            pass
    
    def __init__(self) -> None:
        self.__root=None
        pass

    def insert(self,a):
        temp=self.__node(a)
        temp.next=self.__root
        self.__root=temp
        return

    def delete(self):
        if self.__root==None:
            return
        
        self.__root=self.__root.next
        return

    def traverse(self):

        temp=self.__root
        if temp==None:
            print("Linked list is empty.")
            return

        print("The linked list is : ")
        while temp:
            print(temp.data,end="-> ")
            temp=temp.next
        print()



def main():

    ll=linked_list()
    ll.traverse()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.traverse()
    ll.delete()
    ll.traverse()
    


# main() # Call main function

# Output:
# Linked list is empty.
# The linked list is :
# 3-> 2-> 1->
# The linked list is :
# 2-> 1->
