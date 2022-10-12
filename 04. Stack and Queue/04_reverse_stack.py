
from stack_and_queue import stack

# Problem Statement: Reverse a stack using recursion.

# Algorithm:
# 1. Pop the top element from the stack.
# 2. Reverse the remaining stack.
# 3. Push the popped element at the bottom of the reversed stack.

# Time Complexity: O(n^2)
# Space Complexity: O(n)


# Problem statement : Insert at bottom of stack

# Algorithm:
# 1. If stack is empty push the element and return.
# 2. Pop the top element from the stack.
# 3. Insert the element at the bottom of the stack.
# 4. Push the popped element back to the stack.


def insert_at_bottom(s, data):

    if s.is_empty():
        s.push(data)
        return

    temp = s.pop()
    insert_at_bottom(s, data)
    s.push(temp)


def reverse_stack(s):

    if s.is_empty():
        return

    temp = s.pop()
    reverse_stack(s)
    insert_at_bottom(s, temp)


def main():

    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)
    s.push(8)
    s.push(9)
    s.push(10)
    reverse_stack(s)
    
    for i in range(10):
        print(s.pop(),end=" ")

    print()


main() #calling main function

# Output:
# 1 2 3 4 5 6 7 8 9 10

