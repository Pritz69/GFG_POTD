class Solution:
    def vowelCount(self, s):
        #code here
        def fact(x) :
            if x==0:
                return 0
            p=1
            for i in range(1,x+1) :
                p=p*i
            return p
        f={}
        for x in s :
            if x in "aeiouAEIOU" :
                f[x]=f.get(x,0)+1
        ans=fact(len(f))
        for x in f :
            ans=ans*f[x]
        return ans