 
from stack_and_queue import stack

# Problem Statement: Implement a Queue using two stacks s1 and s2 .

# Solution:
# 1. Enqueue: Push the element into the first stack s1 .
# 2. Dequeue: If the second stack s2 is empty, then push all the elements from s1 to s2 . Pop the element from s2 .


# Time Complexity: O(1) for enqueue and O(n) for dequeue.
# Space Complexity: O(n) for enqueue and O(1) for dequeue.

class queue_using_stack:
    def __init__(self):
        self.s1 = stack()
        self.s2 = stack()

    def enqueue(self, data):
        self.s1.push(data)

    def dequeue(self):

        if self.s2.is_empty():

            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
            
        return self.s2.pop()



def main():
    q = queue_using_stack()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())


main() #calling main function

# Output:
# 1
# 2
# 3
# 4
