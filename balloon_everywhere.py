class Solution:
    def maxInstance(self, s : str) -> int:
        # code here
        m=dict()
        mi=float('inf')
        for i in s :
            if i in "balloon" :
                if i in m :
                    m[i] +=1
                else :
                    m[i] =1
        ans=0
        while(m['b']>=1 and m['a']>=1 and m['l']>=2 and m['o']>=2 and m['n']>=1) :
            ans +=1
            m['b'] -=1
            m['a'] -=1
            m['l'] -=2
            m['o'] -=2
            m['n'] -=1
        return ans
        
