class Solution:
    def reverseWords(self, s: str) -> str:
        l,res=[],[]
        temp=""
        s=s.split(" ")
        for i in s:
            res.append(i[::-1])
    
        return " ".join(res)