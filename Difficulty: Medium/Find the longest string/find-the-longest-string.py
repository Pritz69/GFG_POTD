class Solution():
    def longestString(self, words):
        # code here
        s=set(words)
        l=[]
        for x in words :
            f=0
            for i in range(len(x)) :
               if x[:i+1] not in s :
                   f=1
                   break
            if f==0 :
                l.append(x)
        if l :
            ans=l[0]
        #print(l)
        else :
            ans=""
        for x in l :
            if len(x) > len(ans) :
                ans=x
            elif len(x)==len(ans) :
                if x < ans :
                    ans=x
        return ans
                
        
        