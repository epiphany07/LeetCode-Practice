class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v='aeiouAEIOU'
        m=int(len(s)/2)
        a,b=s[:m],s[m:]
        # print(a,b)
        a1=[i for i in a if i in v]
        b1=[i for i in b if i in v]
        return True if len(a1)==len(b1) else False
        