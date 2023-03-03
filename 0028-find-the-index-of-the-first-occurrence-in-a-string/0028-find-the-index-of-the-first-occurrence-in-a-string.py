class Solution:
    def strStr(self, h: str, n: str) -> int:
        if n not in h:
            return -1
        else:
            j=0
            return h.index(n)
