class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # global m,n
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i==0 or j==0 or i==m-1 or j==n-1) and grid[i][j]==1:
                    check(grid,i,j)
        c=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    c+=1
        return c
def check(ar,i,j):
    m=len(ar)
    n=len(ar[0])
    if i<0 or j<0 or i>=m or j>=n or ar[i][j]==0:
        return
    ar[i][j]=0
    check(ar,i-1,j)
    check(ar,i+1,j)
    check(ar,i,j+1)
    check(ar,i,j-1)
