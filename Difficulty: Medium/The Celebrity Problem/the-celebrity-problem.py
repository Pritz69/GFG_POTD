from collections import defaultdict
class Solution:
    def celebrity(self, mat):
        # code here
        d=defaultdict(set)
        n=len(mat)
        m=len(mat[0])
        for i in range(n) :
            for j in range(m) :
                v=mat[i][j]
                if v==1 :
                    d[i].add(j)
        #print(d)
        l=d.values()
        #print(l)
        ans=-1
        for x in d :
            #print(x,d[x],len(d[x]))
            if len(d[x])==1 :
                l=d.values()
                c=0
                for e in l :
                    #print(e)
                    if x in e :
                        c +=1
                if c==n:
                    ans=x
        return ans
        