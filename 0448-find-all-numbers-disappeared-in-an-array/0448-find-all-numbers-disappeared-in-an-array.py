class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l=set(nums)
        res=[i+1 for i in range(len(nums))]
        r=[]
        for i in range(len(res)):
            if res[i] not in l:
                r.append(res[i])
            else:
                l.remove(res[i])
        return r
    

