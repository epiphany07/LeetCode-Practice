class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=[abs(i) for i in nums]
        l.sort()
        l=[i*i for i in l]
        return l