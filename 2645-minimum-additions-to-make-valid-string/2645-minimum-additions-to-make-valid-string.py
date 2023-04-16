class Solution:
    def addMinimum(self, word: str) -> int:
        # word=word.replace("abc","")
        # print(word)
        c,i=0,0
        l=len(word)
        while i<l:
            # print(i)
            if i>=l or word[i]!='a':
                c+=1
            else:
                i+=1
                # print(i)
            if i>=l or word[i]!='b':
                # print(c)
                c+=1
            else:
                i+=1
            if i>=l or word[i]!='c':
                c+=1
            else:
                i+=1
        return c
            
#         while "ab" in word or "bc" in word or "ac" in word:
            
#             if "ab" in word:
#                 c+=1
#                 word=word.replace("ab","",1)
#             if "bc" in word:
#                 c+=1
#                 word=word.replace("bc","",1)
#             if "ac" in word:
#                 c+=1
#                 word=word.replace("ac","",1)
#         while "a" in word or "b" in word or "c" in word:
            
#             if "a" in word:
#                 c+=2
#                 word=word.replace("a","",1)
#             if "b" in word:
#                 c+=2
#                 word=word.replace("b","",1)
#             if "c" in word:
#                 c+=2
#                 word=word.replace("c","",1)
#         if word=="":
#             return c
        