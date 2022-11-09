
# Problem Statement: You are given a matrix of size N x M, location of a cell in the matrix and a value K.
# Your task is to replace the color of the given cell and all adjacent(excluding diagonally adjacent) same colored cells with the value K.

# Example:
# Input:

# Matrix:
# 1 1 2
# 2 3 2
# 1 1 2

# Source Cell: (0,0) and K = 3

# You have to replace the color of the given cell and all connected points with same colored cells with the value K.


# Output:

# 3 3 2
# 2 3 2
# 1 1 2


# Tags: Graph, Matrix, Flood Fill, DFS, BFS


# Approach: We can use DFS or BFS to solve this problem. We will use DFS in this problem.

# Algorithm:
# 1. Check if the given cell is valid or not. If not, return.
# 2. If the given cell is valid, check if the color of the cell is same as the color of the source cell or not. If not, return.
# 3. If the color of the cell is same as the color of the source cell, replace the color of the cell with the value K.
# 4. Recursively call the function for all the adjacent cells of the current cell.


def flood_fill_helper(matrix,x,y,source_color,dest_color):

    if x<0 or y<0 or x>=len(matrix) or y>=len(matrix[0]):
        return
    
    if matrix[x][y]!=source_color:
        return

    matrix[x][y]=dest_color

    flood_fill_helper(matrix,x+1,y,source_color,dest_color)
    flood_fill_helper(matrix,x-1,y,source_color,dest_color)
    flood_fill_helper(matrix,x,y+1,source_color,dest_color)
    flood_fill_helper(matrix,x,y-1,source_color,dest_color)



def flood_fill(matrix,x,y,k):

    source_color=matrix[x][y]

    flood_fill_helper(matrix,x,y,source_color,k)

    return matrix



# <-- End of Code -->


def main():

    matrix=[[1,1,2],[2,3,2],[1,1,2]]
    x=0
    y=0
    k=3

    ans=flood_fill(matrix,x,y,k)

    for i in ans:
        print(*i)


main() # calling main function


# Output:

# 3 3 2
# 2 3 2
# 1 1 2