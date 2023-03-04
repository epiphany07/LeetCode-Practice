class Solution:
    def countSubarrays(self, n: List[int], minK: int, maxK: int) -> int:

        l,mip,map=-1,-1,-1
        res=0
        for i,num in enumerate(n):
            if num >maxK  or num<minK:
                l=i
            if num==minK:
                mip=i
            if num==maxK:
                map=i
            res+=max(0,min(mip,map)-l)
        return res


















#         c=0
#         res=0
#         if len(set(n))==1:
#             return int((len(n)*(len(n)+1)/2))
#         for i in range(len(n)):
#             if n[i]>=minK and n[i]<=maxK:
#                 c+=1
#             else:
#                 c=0
#             res=max(res,c)
#         return res-2

        
        