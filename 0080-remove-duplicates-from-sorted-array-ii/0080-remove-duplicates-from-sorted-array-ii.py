class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            d[i]=nums.count(i)
        nums[:]=[]
        print(nums)

        for k,v in d.items():
            print(k,v)
            # print(s)
            nums.extend([k for i in range(v) if i<=1])
        nums.sort()
        print(nums)
        return len(nums)
        