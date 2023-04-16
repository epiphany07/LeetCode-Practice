class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        w1=list(word1)[::-1]
        w2=list(word2)[::-1]
        print(w1,w2)
        while w1 and w2:
            res=res+w1.pop()+w2.pop()
        if w1:
            w1=w1[::-1]
            res+="".join(w1)
        if w2:
            w2=w2[::-1]

            res+="".join(w2)
        return res