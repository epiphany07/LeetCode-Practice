class Solution:
    def maxDistance(self, n1: List[int], n2: List[int]) -> int:
        i,j=0,0
        res=0
        while i<=j and i<len(n1) and j<len(n2):
            if n1[i]<=n2[j]:
                res=max(res,j-i)
                j+=1
                continue
                
            i+=1
            j+=1
        return res
            