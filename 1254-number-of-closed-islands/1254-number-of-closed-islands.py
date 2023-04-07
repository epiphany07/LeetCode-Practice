class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        c=0
        v=[]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if ( grid[i][j]==0 and dfs(grid,i,j)):
                    c+=1
        return c
def dfs(ar,i,j):
    if i<0 or j<0 or i>=len(ar) or j>=len(ar[0]):
        return False
    if ar[i][j]==1:
        return True
    ar[i][j]=1
    # v[i][j]=True
    a=dfs(ar,i+1,j)
    b=dfs(ar,i-1,j)
    c=dfs(ar,i,j+1)
    d=dfs(ar,i,j-1)
    return a and b and c and d