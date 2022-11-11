class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:]=sorted(set(nums))
        k=len(nums)
        # for i in range(1,len(nums)-1):
        #     if nums[i]==nums[i-1]:
        #         j=i
        #     if nums[i+1]!=nums[i]:
        #         nums[j]=nums[i+1]
        return k
              
        
        
        