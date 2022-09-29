class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        print(k,x)
        if x<=arr[0]:
            return arr[:k]
        else:
            res=[]
            # for i in range(1,len(arr)):
                
#                 a=arr[i-1]
#                 b=arr[i]
#                 print(arr[i:i+4])
#                 print(abs(a-x),abs(b-x))
#                 if abs(a-x)>=abs(b-x) and a<b :
#                     return arr[i-1:i+k-1]
            #     res.append(abs(arr[i-1]-x))
            # print(res)
            # d=dict(zip(arr,res))
            # print(d)
            # return sorted(d)[:k]
            t = sorted(arr,key=lambda i:abs(i-x)) 
        print(t)
        return sorted(t[:k])
        
            