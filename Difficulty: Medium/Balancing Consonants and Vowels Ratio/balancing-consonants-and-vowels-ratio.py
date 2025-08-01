from collections import defaultdict
class Solution:
    def countBalanced(self, arr):
        # code here
        l=[]
        for x in arr :
            c,v=0,0
            for y in x :
                if y in "aeiou" :
                    v +=1
                else :
                    c +=1
            l.append(c-v)
        
        d=defaultdict(int)
        d[0]=1
        s=0   
        ans=0
        for x in l :
            s += x
            if s in d :
               ans += d[s]
            d[s] +=1
        return ans
