class Solution:
    def splitString(self, n, s):
        # code here
        a=dict()
        b=dict()
        for i in s :
            if i in b :
                b[i] +=1 
            else :
                b[i] =1 
                a[i] =0
        ans=0
        for i in s :
            a[i] +=1
            b[i] -=1
            c=0
            for x in b :
                if b[x]>0 and a[x]>0 :
                    c +=1
            ans = max(ans,c)
        return ans
