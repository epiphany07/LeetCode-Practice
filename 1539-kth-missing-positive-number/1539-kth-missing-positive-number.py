class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        h=arr[-1]
        res=[]
        l=arr[0]
        res=[i+1 for i in range(h)]
        for i in arr:
            res.remove(i)
        # print(res)
        if res==[]:
            return h+k
        elif len(res)<k:
            x=[i for i in range(h+1,h+k-len(res)+1)]
            res.extend(x)
        else:
            pass
        print(res)

        return res[k-1]

        # for i in range(len(arr)):
        #     if i+l!=arr[i]:
        #         res.append(i+l)
        # print(res)
        # if res==[]:
        #     return h+k
        # if res[-1]<h:
        #     x=[i for i in range(res[-1]+2,h)]
        # res.extend(x)
        # print(res)
        # return res[k-1]

