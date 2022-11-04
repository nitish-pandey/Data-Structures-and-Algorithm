
# Problem Statement: N-Queens
# You are given an empty chess board of size n*n. You have to place n queens on this board in such a way that no queen can kill other.


# Tags:  Backtracking


# Algorithm:

# 1. isSafe Function will check if the current cell is safe or not.
#     a. Check for the column
#     b. Check for the left diagonal
#     c. Check for the right diagonal


# 2. n_queens_helper Function will place the queens recursively in the board.
#     a. If x>=n then return True.
#     b. Iterate over the columns and check if the current cell is safe or not.
#     c. If the current cell is safe then place the queen and call the n_queens_helper function for the next row.
#     d. If the current cell is not safe then backtrack and remove the queen from the current cell.
#     e. If the current cell is not safe and we have tried all the columns then return False.


# 3. n_queens Function will call the n_queens_helper function and print the solution if it exists.
#    a. Create a board of size n*n.
#    b. Call the n_queens_helper function.
#    c. If the solution exists then print the board else print "No Solution Exists".



# Time Complexity: O(n!)
# Space Complexity: O(n*n)

board=[]


def isSafe(x:int,y:int,n:int) ->bool:

    global board

    # Check for the column
    for i in range(x):
        if board[i][y]==1:
            return False

    # Check for the left diagonal
    i=x
    j=y

    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1

    # Check for the right diagonal
    i=x
    j=y

    while i>=0 and j<n:
        if board[i][j]==1:
            return False
        i-=1
        j+=1

    return True




def n_queens_helper(x:int,n:int) ->bool:

    global board

    if x>=n:
        return True

    for i in range(n):
        if isSafe(x,i,n):
            board[x][i]=1

            if n_queens_helper(x+1,n):
                return True

            board[x][i]=0

    return False




def n_queens(n:int):

    global board

    board=[[0 for i in range(n)] for j in range(n)]

    if n_queens_helper(0,n):

        print("The Solution is: ")
        for i in range(n):
            for j in range(n):
                print(board[i][j],end=" ")
            print()

        
    else:
        print("No Solution Exists")

    



def main():

    n=4

    n_queens(n)



main() # call to main function


# Output: 

# The Solution is:
# 0 1 0 0
# 0 0 0 1
# 1 0 0 0
# 0 0 1 0