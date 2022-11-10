class Solution:
    def calPoints(self, op: List[str]) -> int:
        res=[]
        for i in op:
            if i=="+" and res:
                res.append(res[-1]+res[-2])
            elif i=="D":
                res.append(res[-1]*2)
            elif i=="C":
                res.pop()
            else:
                res.append(int(i))
                
        return sum(res)