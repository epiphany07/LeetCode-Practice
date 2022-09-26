class Solution:
    
    def equationsPossible(self, eq: List[str]) -> bool:
        
#         ind,x=[],{}
#         eq.sort(key = lambda x: x[1],reverse=True)
#         print(eq)
#         for i in range(len(eq)):
#             ind.append(i)
#             s=eq[i]
#             if s[0] == s[3] and s[1]=='!':
#                 return False
#             elif s[0] == s[3] and s[1]=='=':
#                 x[s[0]]=s[3]
#                 print(1)
#             elif s[0]!=s[3] and (s[1]!='!'):
#                 if x[s[0]] in x.values():
#                     x[[i for i in dic if dic[i]==s[3]]] = s[0]
#                 x[s[0]]=s[3]
                
#                 # x.append(s[3])
#                 print(x)
#                 continue

#             else:
#                 print(s[0] in x.values())
#                 if s[0] in x.values():
#                     return False
#                 elif( s[0] in x and x[s[0]]==s[3]):
#                     print(2)
#                     return False
#                 else:
#                     return True
#         print(1)
#         return True
        parent = {}
        def find(x):
            parent[x] = parent.get(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x]) ##path compression
            return parent[x]
        def union(u, v):
            parent[find(u)] = find(v)
        for eqn in eq:
            if eqn[1] == "=":
                union(eqn[0], eqn[3])
        for eqn in eq:
            if eqn[1] == "!":
                if find(eqn[0]) == find(eqn[3]):
                    return False
        return True