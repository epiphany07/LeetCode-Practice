class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res=[]
        
        # if "d1/" not in  logs:
        #     return 0
        for i in logs:
            if i=="../" and res:
                res.pop()
            elif i=="./":
                pass
            elif i!="./" and i!="../":
                res.append(i)
        print(res)
    
        return len(res)
                