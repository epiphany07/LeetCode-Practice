class Solution:
    def isValid(self, s: str) -> bool:
        
        # if s=="":
        #     return True
        # while '{}' in s or '[]' in s or '()' in s:
        # # for i in range(len(s)//2):
        #     # if s=='': return True
        #     s.replace("{}","").replace("[]","").replace("()","")
        # return not bool(s)
        while s != '':
            t = s
            s = s.replace('()','')
            s = s.replace('[]','')
            s = s.replace('{}','')
            if s == t:
                return False
        return True
                
                    
            
                
        