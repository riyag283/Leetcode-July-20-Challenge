def numofneigh(mat,i,j,R,C):
    count = 0; 
    if (i > 0 and mat[i - 1][j]): 
        count+= 1; 
    if (j > 0 and mat[i][j - 1]): 
        count+= 1; 
    if (i < R-1 and mat[i + 1][j]): 
        count+= 1
    if (j < C-1 and mat[i][j + 1]): 
        count+= 1; 
    return count;

def func(grid):
    perimeter = 0
    R = len(grid)
    C = len(grid[0])
    for i in range(0,R):
        for j in range(0,C):
            if grid[i][j]:
                perimeter += (4 - numofneigh(grid,i,j,R,C))
    return perimeter

mat = [ [0, 1, 0, 0, 0], 
        [1, 1, 1, 0, 0], 
        [1, 0, 0, 0, 0] ] 
  
print(func(mat), end="\n")
