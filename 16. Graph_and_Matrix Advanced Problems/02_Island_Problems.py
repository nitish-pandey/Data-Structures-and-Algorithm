
# You are given a matrix of size N x M. The 1s in the matrix represent land and 0s represent water. 
# Note: You can assume that all 4 edges of the matrix are surrounded by water.
# The Lands can be connected either horizontally or vertically but not diagonally.



# Problem Statement 1: Find the number of islands in the given matrix.

# Example:
# Input:
# 1 1 0 0 0
# 0 1 0 0 1
# 1 0 0 1 1
# 0 0 0 0 0

# Output: 3

# Approach : Using DFS

# Time Complexity : O(n*m)
# Space Complexity : O(n*m)

# Algorithm for DFS :
# 1. Check if the out of bound condition is satisfied or not, if not then return.
# 2. Check current cell is land or not, if not then return.
# 3. Change the current cell to water.
# 4. Call the dfs function for all the 4 directions.


# Algorithm:
# Call the DFS function for each cell of the matrix and increment the count variable by 1 if the current cell is land.


def dfs_1(grid:list(list(int)),i:int,j:int):

    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0:
        return

    grid[i][j]=0

    dfs_1(grid,i+1,j)
    dfs_1(grid,i-1,j)
    dfs_1(grid,i,j+1)
    dfs_1(grid,i,j-1)

    return

def no_of_Islands(grid:list(list(int))) -> int:

    n=len(grid)
    m=len(grid[0])
    count=0

    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                dfs_1(grid,i,j)
                count+=1


    return count



#Problem Statement 2: Find the Perimeter of the island.

# Problem Statement 3: Find the maximum area of the island.