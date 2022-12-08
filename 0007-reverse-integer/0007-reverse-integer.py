class Solution:
    def reverse(self, x: int) -> int:
        
        if x<0:
            x=abs(x)
            s=str(x)
            return -int(s[::-1]) if (-int(s[::-1])>-2147483648)  else  0
        s=str(x)
        return int(s[::-1]) if (int(s[::-1])<2147483647) else  0
        