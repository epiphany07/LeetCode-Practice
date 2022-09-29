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
            # d=dict(zip(arr,res))
            # print(d)
            # return sorted(d)[:k]
            Result = sorted(arr,key=lambda y:abs(y-x)) 
        print(Result)
        #Take the first k elements & return them in sorted order 
        return sorted(Result[:k])
        
            