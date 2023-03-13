class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        l=permutations(nums)
        res=[]
        for i in l:
            if i not in res:
                res.append(i)
        return res
        