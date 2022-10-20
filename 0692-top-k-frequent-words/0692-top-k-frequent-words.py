class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d={}
        for i in range(len(words)):
            d[words[i]]=words.count(words[i])
        print(d)
        l = sorted(d, key = lambda i: (-d[i], i))
        return l[:k]
#         d=dict(sorted(d.items(), key=lambda d: d[1],reverse = True))
#         for i in d:
#             if d[i]
#         print(l)
        
        
        # return l[:k]
        # return sorted(l,key=lambda l:l[1])