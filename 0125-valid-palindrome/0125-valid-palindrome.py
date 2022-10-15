class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
         'r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
        n=[]
        for i in range(len(s)):
            if s[i] in a:
                n.append(s[i])
        if n==n[::-1]:
            return True
        else:
            return False
        