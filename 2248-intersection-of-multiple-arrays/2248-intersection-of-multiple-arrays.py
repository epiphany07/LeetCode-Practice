class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res=[]
        # for n in range(1,len(nums)):
        #     for i in nums[0]:
        #         if i in nums[n]:
        #             res.append(i)
        #             break
        l=[element for sublist in nums for element in sublist]
        k=sorted(list(set(l)))
        for i in k:
            if l.count(i)==len(nums):
                res.append(i)

        return res