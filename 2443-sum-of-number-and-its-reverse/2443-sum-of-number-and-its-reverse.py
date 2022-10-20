class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num==0:
            return True
        else:
            for i in range(1,num):
                if num-i==int(str(i)[::-1]):
                    return True
        return False
        