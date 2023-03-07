class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        if cost1 >total and cost2>total:
            return 1
        else:
            x=max(cost1,cost2)
            y=min(cost1,cost2)
            xc,yc=0,0
            a=total//x
            b=total//y
            for i in range(1,a+1):
                b+=(total-(i*x))//y+1

        return b+1
                
                

