# import permutations from itertools

class Solution:
    # @fp.lru_cache(None)

    def findLength(self, l1: List[int], l2: List[int]) -> int:
        
#         dp = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)]

#         mx = 0
#         for i in range(1,len(nums1)+1):
#             for j in range(1,len(nums2)+1):
#                 if nums1[i-1] == nums2[j-1]:
#                     dp[i][j] = dp[i-1][j-1] + 1
#                     if dp[i][j] > mx:
#                         mx = dp[i][j]
#         return mx
        
        
        
        
        
        # @lru_cache(None)
        if l1==l2:
            return len(l1)
        else:
            a=len(l1)
            b=len(l2)
            c=0
            dp=[[0 for i in range(b+1)] for j in range(a+1)]
            # dp = np.zeros((len(l1)+1,len(l2)+1), dtype = int)
            # print(dp)
            for i in range(1,a+1):
                for j in range(1,b+1):
                    if l1[i-1]==l2[j-1] : 
                        dp[i][j]=dp[i-1][j-1]+1
                        if dp[i][j] > c:
                            c = dp[i][j]
                    
            return c

                        
                    
            