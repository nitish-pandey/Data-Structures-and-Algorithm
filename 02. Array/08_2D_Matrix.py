
# 2D array is a special form of 1D array. It is a collection of 1D arrays.
# 2D array is also called as Matrix.
# 2D array is a collection of rows and columns.


# Problem Statement 1: Print the matrix in spiral form

# Algorithm:
# 1. Take 4 variables i,j,k,l and initialize them to 0,0,n-1,m-1 respectively.
# 2. Run a loop while i<=k and j<=l.
# 3. Print the elements of the first row from j to l.
# 4. Print the elements of the last column from i+1 to k.
# 5. Print the elements of the last row from l-1 to j-1 if i!=k.
# 6. Print the elements of the first column from k-1 to i+1 if j!=l.
# 7. Increment i,j by 1 and decrement k,l by 1.


def print_spiral_matrix(matrix: list) -> None:

    n=len(matrix)
    m=len(matrix[0])

    i,j,k,l=0,0,n-1,m-1

    while i<=k and j<=l:

        for p in range(j,l+1):
            print(matrix[i][p],end=" ")

        for p in range(i+1,k+1):
            print(matrix[p][l],end=" ")

        if i!=k:
            for p in range(l-1,j-1,-1):
                print(matrix[k][p],end=" ")

        if j!=l:
            for p in range(k-1,i,-1):
                print(matrix[p][j],end=" ")

        i+=1
        j+=1
        k-=1
        l-=1

    print()


    

def main():

    matrix=[
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]

    print_spiral_matrix(matrix)

