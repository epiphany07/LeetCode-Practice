class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # res=[ nums1[i] for i in range(len(nums1)) if nums1[i] in nums2 ]
        res=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                nums2.remove(nums1[i])
                res.append(nums1[i])
        return res