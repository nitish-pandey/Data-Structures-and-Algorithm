
# Problem Statement : You are given an N x M matrix. Each cell (i, j) in the matrix can have one of three values:
# 0, 1 or 2, which has the following meaning:
# 0 : Empty cell
# 1 : Cells have fresh oranges
# 2 : Cells have rotten oranges
# Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1 instead. 

# Example:
# Input:[
# [2,1,1],
# [1,1,0],
# [0,1,1]]

# Output: 4


# Tags: BFS, DFS, Graph, Matrix

# Approach: Using BFS

# Algorithm:
# 1. Find all rotten oranges and add them to the queue
# 2. For each rotten orange, find all fresh oranges adjacent to it and add them to the queue
# 3. Repeat step 2 until queue is empty
# 4. Return the number of minutes elapsed


# Time Complexity : O(n*m)
# Space Complexity : O(n*m)


def rotten_oranges(grid:list()) ->int:

    n=len(grid)
    m=len(grid[0])

    queue=[]

    for i in range(n):
        for j in range(m):
            if grid[i][j]==2:
                queue.append((i,j))
    

    curr_time=0

    while queue:

        curr_time+=1

        for _ in range(len(queue)):

            i,j=queue.pop(0)

            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:

                if 0<=x<n and 0<=y<m and grid[x][y]==1:
                    grid[x][y]=2
                    queue.append((x,y))


    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                return -1

    # if no rotten oranges

    if curr_time==0:
        return 0

    return curr_time-1




def main():

    grid=[ [2,1,1], [1,1,0], [0,1,1] ]

    print(rotten_oranges(grid))



main() # Call to main() function

# Output: 4