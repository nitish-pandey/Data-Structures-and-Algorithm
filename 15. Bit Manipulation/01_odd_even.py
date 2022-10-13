
# Basic Understanding: If the number is Odd its last bit will be 1, else it will be 0 for Even  


# Problem Statement: Find the parity of a number using bitwise OR operator

# Algorithm
# 1. We find the bitwise OR of the number with 1 (i.e. n | 1)
# 2. If the result is same as the number, then the number is Odd
# 3. Else the number is Even


def odd_even_using_or(n):

    if n<0:
        print("Invalid")
        return


    a= n | 1

    if a==n:
        print("Odd")

    else:
        print("Even")

    return
    


# Problem Statement: Find the parity of a number using bitwise AND operator

# Algorithm
# 1. We find the bitwise AND of the number with 1 (i.e. n & 1)
# 2. If the result is 1, then the number is Odd
# 3. Else the number is Even


def odd_even_using_and(n):

    if n<0:
        print("Invalid")
        return

    a=n & 1

    if a:
        print("Odd")

    else:
        print("Even")

    return
    


# Problem Statement: Find the parity of a number using bitwise XOR operator

# Algorithm: 
# 1. We find the bitwise XOR of the number with 1 (i.e. n ^ 1)
# 2. If the result is same as the number+1, then the number is Even
# 3. Else the number is Odd

def odd_even_using_xor(n):

    if n<0:
        print("Invalid")
        return

    
    a= n ^ 1

    if a==n+1:
        print("Even")

    else:
        print("Odd")

    return





def main():

    n= 45707

    odd_even_using_or(n)
    odd_even_using_and(n)
    odd_even_using_xor(n)

    return



main() # call to main function

# Output:
# Odd
# Odd
# Odd

