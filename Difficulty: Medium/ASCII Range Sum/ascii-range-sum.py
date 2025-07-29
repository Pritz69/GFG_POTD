from collections import defaultdict
class Solution:
    def asciirange(self, s):
        # code here
        d=defaultdict(list)
        for i,x in enumerate(s) :
            d[x].append(i)
        ans=[]
        for x in d :
            if len(d[x]) > 1 :
                i,j=d[x][0],d[x][-1]
                c=0
                i=i+1
                while i < j :
                    c += ord(s[i])
                    i +=1
                if c > 0 :
                    ans.append(c)
        return ans
            