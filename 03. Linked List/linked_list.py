
class linked_list:

    class node:

        def __init__(self, data):

            self.data=data
            self.next=None

    def __init__(self):

        self.head=None

    def insert(self, data):

        temp=self.node(data)

        temp.next=self.head
        self.head=temp

    def print_list(self):

        temp=self.head

        while temp:
            print(temp.data, end=" ")
            temp=temp.next

        print()

    def insert_last(self, data):

        temp=self.node(data)

        if self.head==None:
            self.head=temp
            return

        ptr=self.head

        while ptr.next:
            ptr=ptr.next

        ptr.next=temp

        
