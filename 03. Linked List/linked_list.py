

class node:

    def __init__(self, data=-1):

        self.data=data
        self.next=None


class linked_list:



    def __init__(self):

        self.head=None

    def insert(self, data):

        temp=node(data)

        temp.next=self.head
        self.head=temp

    def print_list(self):

        temp=self.head

        print("\nThe Linked list is : ")

        while temp:
            print(temp.data, end=" -> ")
            temp=temp.next

        print(" NULL")

    def insert_last(self, data):

        temp=node(data)

        if self.head==None:
            self.head=temp
            return

        ptr=self.head

        while ptr.next:
            ptr=ptr.next

        ptr.next=temp

        
