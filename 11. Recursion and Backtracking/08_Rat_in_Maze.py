

# Problem Statement: Rat in Maze
# You are given n*m maze with a rat placed at maze[0][0]. 
# Find and print paths that rat can follow to reach its destination i.e. maze[n-1][m-1]. 
# Rat can move in any direction ( left, right, up and down).

# Tags:  Backtracking

# Approach: We will use backtracking to solve this problem.

# Backtracking is an algorithmic-technique for solving problems recursively by trying to build a solution incrementally, 
# one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time 
# (by time, here, is referred to the time elapsed till reaching any level of the search tree).


# Algorithm:
# 1. We will create two global 2D array path and visited of size n*m intialized with 0.
# 2. We will create a helper function which will take the maze, x and y coordinates, n and m as parameters.
# 3. We will check if the x and y coordinates are valid or not, if not then we will return False.
# 4. We will check if the current cell is the destination cell or not, if yes then we will return True.
# 5. We will check if the current cell is already visited or not, if yes then we will return False.
# 6. We will mark the current cell as visited.
# 7. We will call the helper function recursively for all the four directions.
# 8. If any of the recursive call returns True then we will mark the current cell as 1 in the path matrix and return True.
# 9. If none of the recursive call returns True then we will return False.


# Time Complexity: O(2^(n*m))
# Space Complexity: O(n*m)


path=[]
visited=[]


def rat_in_maze_helper(maze:list,x:int,y:int,n:int,m:int) ->bool:

    global path,visited

    # Check if safe or valid
    if x>=n or y>=m:
        return False
    
    if maze[x][y]==0:
        return False

    if x==n-1 and y==m-1:
        path[x][y]=1
        return True

    if visited[x][y]==1:
        return False

    visited[x][y]=1

    a=rat_in_maze_helper(maze,x+1,y,n,m)
    b=rat_in_maze_helper(maze,x,y+1,n,m)
    c=rat_in_maze_helper(maze,x-1,y,n,m)
    d=rat_in_maze_helper(maze,x,y-1,n,m)

    if a or b or c or d:
        path[x][y]=1
        return True


    return False

     


def rat_in_maze(maze):

    n=len(maze)
    m=len(maze[0])

    global path,visited

    path=[[0 for i in range(m)] for j in range(n)]
    visited=[[0 for i in range(m)] for j in range(n)]


    rat_in_maze_helper(maze,0,0,n,m)

    print("The Path is: ")

    for i in range(n):
        for j in range(m):
            print(path[i][j],end=" ")
        print()




def main():

    maze=[[1,0,1,1,1],
          [1,1,1,0,1],
          [0,0,0,0,1],
          [1,1,1,1,1]]

    rat_in_maze(maze)



main() # calling main function

# Output:

# The Path is: 

# 1 0 1 1 1 
# 1 1 1 0 1 
# 0 0 0 0 1 
# 0 0 0 0 1 