class Solution:
    def largestMerge(self, w1: str, w2: str) -> str:
        res=""
        for i in range(len(w1)+len(w2)):
            if w1>w2:
                res+=w1[0]
                w1=w1[1:]
            else:
                res+=w2[0]
                w2=w2[1:]
        return res
                        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if w1=="" and w2=="":
#             return ""
#         elif w1 and w2:
#             # if large(w1[0],w2[0])==w1[0]:
#             if len(w2)>len(w1):
#                 # res+=(w1[0]+w2[0])
#                 # w1=w1[0:],w2=w2[0:]
#                 for i in range(0,len(w1)):
#                     if w1[i]==w2[i]:
#                         res+=(w1[i])
#                     elif large(w1[i],w2[i])==w1[i]:
#                         res+=(w1[i]+w2[i])
                        
#                     else:
#                         res+=(w2[i]+w1[i])
#                 if w2:
#                     res+=(w2[i+1:])
#             elif len(w2)<len(w1):
#                 # res+=(w2[0]+w2[0])
#                 # w1=w1[0:],w2=w2[0:]
#                 for i in range(0,len(w2)):
#                     if w1[i]==w2[i]:
#                         res+=w1[i]
#                     elif large(w1[i],w2[i])==w2[i]:
#                         res+=(w2[i]+w1[i])
                        
#                     else:
#                         res+=(w1[i]+w2[i])
#                 if w1:
#                     res+=(w1[i+1:])
#             else:
#                 if large(w1[0],w2[0])==w1[0]:
#             # if len(w2)>len(w1):
#                     res+=(w1[0]+w2[0])
#                     # w1=w1[0:],w2=w2[0:]
#                     for i in range(1,len(w1)):
#                         if large(w1[i],w2[i])==w1[i]:
#                             res+=(w1[i]+w2[i])

#                         else:
#                             res+=(w2[i]+w1[i])
#                     if w2:
#                         res+=(w2[i+1:])
#                 else:
#                     res+=(w2[0]+w2[0])
#                     # w1=w1[0:],w2=w2[0:]
#                     for i in range(1,len(w2)):
#                         if large(w1[i],w2[i])==w2[i]:
#                             res+=(w2[i]+w1[i])

#                         else:
#                             res+=(w1[i]+w2[i])
#                     if w1:
#                         res+=(w1[i+1:])
#             return res
#         else:
#             return w1+w2

                                                            

                              
    
                    
            
            
            
def large(a,b):
    if ord(a)>ord(b):
        return a
        