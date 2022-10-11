class Solution:
    def increasingTriplet(self, n: List[int]) -> bool:
        a=b=2**31-1
        print(a)
        for i in range(len(n)):
            if n[i]<=a:
                a=n[i]
            elif n[i]<=b:
                b=n[i]
            else:
                return True
        return False
        
        
        
                