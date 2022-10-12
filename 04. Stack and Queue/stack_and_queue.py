

class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class stack:

    def __init__(self):
        self.head = None

    def push(self, data):
        if self.head is None:
            self.head = node(data)
        else:
            new_node = node(data)
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            return temp.data

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def is_empty(self):
        return self.head is None

    def print_stack(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def reverse_stack(self):
        if self.head is None:
            return None
        else:
            temp = self.pop()
            self.reverse_stack()
            self.insert_at_bottom(temp)

    def insert_at_bottom(self, data):
        if self.head is None:
            self.push(data)
        else:
            temp = self.pop()
            self.insert_at_bottom(data)
            self.push(temp)




class queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if self.head is None:
            self.head = node(data)
            self.tail = self.head
        else:
            new_node = node(data)
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            return temp.data

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.data

    def is_empty(self):
        return self.head is None

    def size(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
    

    def print_queue(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def reverse_queue(self):
        if self.head is None:
            return None
        else:
            temp = self.dequeue()
            self.reverse_queue()
            self.enqueue(temp)

    def reverse_queue_efficient(self):
        if self.head is None:
            return None
        else:
            stack = []
            while self.head is not None:
                stack.append(self.dequeue())
            while stack:
                self.enqueue(stack.pop())