class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]

        for i,c in Counter(nums).items():
            if c==2:
                res.append(i)
        return res
