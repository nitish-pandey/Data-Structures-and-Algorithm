
from stack_and_queue import queue

# Problem statement: Implement a stack using two queues

# Algorithm:
# 1. Push: Push the element into the first queue q1 .
# 2. Pop: 
#       i. If the first queue q1 has only one element, then pop the element from q1 and return it.
#       ii. If the first queue q1 has more than one element, then pop all the elements from q1 and push them into the second queue q2 .
#       iii. Pop the last element from q1 and return it. Swap the names of the two queues q1 and q2 .


# Time Complexity: O(1) for push and O(n) for pop
# Space Complexity: O(n)



class stack_using_queue:

    def __init__(self):
        self.q1 = queue()
        self.q2 = queue()

    def push(self, data):
        self.q1.enqueue(data)

    def pop(self):

        if self.q1.size() == 1:
            return self.q1.dequeue()

        while self.q1.size() > 1:
            self.q2.enqueue(self.q1.dequeue())

        temp = self.q1.dequeue()

        self.q1, self.q2 = self.q2, self.q1

        return temp




def main():
    s = stack_using_queue()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())


main() # calling main function

# Output:
# 4
# 3
# 2
# 1
