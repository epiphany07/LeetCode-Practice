class Solution:
    def countEven(self, num: int) -> int:
        c=0
        def check(n):
            # if n<10 and n%2==0:
            #     return True
            # elif n<10:
            #     return False
            s=list(str(n))
            d=['1','3','5','7','9']
            b=['0','2','4','6','8',]

            count=0
            print(s)
            for i in s:
                # print(i,end=" ")
                count+=int(i)
            
            if count%2==0:
                return True
            else:
                return False
        for i in range(1,num+1):
            if check(i):
                print(i)
                c+=1
        return c