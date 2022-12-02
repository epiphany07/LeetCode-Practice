class Solution:
    def closeStrings(self, w1: str, w2: str) -> bool:
        if len(w1)!=len(w2):
            return False
        else:
            s1=set(w1)
            s2=set(w2)
            if s1 == s2:
                
                a=[w1.count(i) for i in s1 and s2]
                b=[w2.count(i) for i in s2 and s1]
                a.sort()
                b.sort()
                print(a,b)
                return True if a==b else False