
from stack_and_queue import queue

# Problem Statement: Reverse a queue using recursion

# Algorithm:
# 1. Pop the first element from the queue
# 2. Reverse the queue
# 3. Append the element to the queue

# Time Complexity:     O(n)
# Space Complexity:    O(n)


def reverse_queue(q):

    if q.is_empty():
        return

    data = q.dequeue()
    reverse_queue(q)
    q.enqueue(data)


def main():
    q = queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(9)
    q.enqueue(10)
    reverse_queue(q)
    
    for i in range(10):
        print(q.dequeue(),end=" ")

    print()


main() #calling main function

# Output:
# 10 9 8 7 6 5 4 3 2 1

