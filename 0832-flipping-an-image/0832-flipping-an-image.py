class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res=[]
        for i in range(len(image)):
            x=[1 if i==0 else 0 for i in image[i] ]
            print(x)
            x.reverse()
            # print(x.reverse())

            res.append(x)
        return res
            

        