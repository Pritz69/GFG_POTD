from collections import Counter
class Solution:
    def find_permutation(self, S):
        # Code here
        c=Counter(list(S))
        ans=[]
        p=[]
        def dfs() :
            if len(p) == len(S) :
                x=p.copy()
                ans.append(''.join(x))
                return 
            for i in c :
                if c[i]>0 :
                    p.append(i)
                    c[i] -=1
                    dfs()
                    p.pop()
                    c[i] +=1
        dfs()
        return sorted(ans)
