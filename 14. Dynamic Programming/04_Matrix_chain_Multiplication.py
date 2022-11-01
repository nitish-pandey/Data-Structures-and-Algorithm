
# Problem Statement: Given a sequence of matrices, find the most efficient way to multiply these matrices together. 
# The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications.


# Approach: Dynamic Programming
# We will use a 2D array to store the minimum number of multiplications required to multiply the matrices from i to j
# We will use a 2D array to store the index of the matrix after which we will split the matrices from i to j



def matrix_multiplication(dims:list) ->int:

    n=len(dims)-1

    if n<2:
        return 0
    
    m_table=[[0]*(n+1) for _ in range(n+1)]

    