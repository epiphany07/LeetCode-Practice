class Solution:
    def isToeplitzMatrix(self, mat: List[List[int]]) -> bool:
        c=len(mat)
        r=len(mat[0])
        i,j=1,1
        # while i<c and j<r:
        #     if mat[i][j]!=mat[i-1][j-1]:
        #         return False
        #     i+=1
        #     j+=1
        for i in range(1,c):
            for j in range(1,r):
                if mat[i][j]!=mat[i-1][j-1]:
                    return False

            
        return True