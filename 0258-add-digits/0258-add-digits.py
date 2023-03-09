class Solution:
    def addDigits(self, n: int) -> int:
        if n==0:
            return 0
        return n%9 if n%9!=0 else 9

        