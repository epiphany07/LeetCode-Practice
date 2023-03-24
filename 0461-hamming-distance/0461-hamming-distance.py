class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c=x^y
        return bin(c).count('1')
