class MedianFinder(object):

    def __init__(self):
        self.l=[]

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.l.append(num)
        
        

    def findMedian(self):
        """
        :rtype: float
        """
        self.l.sort()
        s=len(self.l)
        print(s)
        if s%2!=0:
            print(1)
            return self.l[int((s-1)/2)]
        else:
            m=s//2
            return float(self.l[m]+self.l[m-1])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()