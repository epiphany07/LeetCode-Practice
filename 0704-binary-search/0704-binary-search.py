class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     return -1
        l,h=0,len(nums)-1
        if l==h:
            if nums[0]==target:
                return 0
            else:
                return -1

        while(l<=h):
            m=int((l+h)/2)
            print(m)
            if nums[m]==target:
                return m
            if nums[m]<target:
                l=m+1
            else:
                h=m-1
        return -1