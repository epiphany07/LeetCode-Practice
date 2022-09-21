class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res=[]
        ev=0
        [ev:=ev+i for i in nums if i&1==0]
        # 
        for l in queries:
            if nums[l[1]]&1==0:
                ev=ev-nums[l[1]]
            nums[l[1]]+=l[0]
            if nums[l[1]]&1==0:
                ev=ev+nums[l[1]]
            res.append(ev)
        return res
def even(l):
    s=0
    [s:=s+i for i in l if i&1==0]
    # print(s)
    return s
            
        