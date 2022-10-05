class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)
        # s=[i for i in range(0,l+1)]
        # print(s)
        # s1=sum(s)
        # # nums.sort()
        # x=[i for i in s if i not in nums]
        # return(x[0])
        s1=int(l*(l+1)/2)
        x=sum(nums)
        return s1-x
        