class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res,r=[],[]
        for i in s:
            if i=='#' and res:
                res.pop()
            elif i!='#':
                res.append(i)
        for i in t:
            if i=='#' and r:
                r.pop()
            elif i!='#':
                r.append(i)
        return ''.join(res)==''.join(r)