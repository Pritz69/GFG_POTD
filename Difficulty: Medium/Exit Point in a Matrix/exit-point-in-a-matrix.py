class Solution:
    def exitPoint(self, mat):
        # code here
        n=len(mat)
        m=len(mat[0])
        l=[0,-1]
        r=[0,1]
        u=[-1,0]
        do=[1,0]
        last=[]
        def func(i,j,d) :
            nonlocal last
            if i<0 or i >=n or j<0 or j>=m :
                return last
            last=[i,j]
            if mat[i][j]==0 :
                return func(i+d[0],j+d[1],d)
            else :
                mat[i][j]=0
                if d==[0,1]:
                    return func(i+do[0],j+do[1],do)
                elif d==[1,0] :
                    return func(i+l[0],j+l[1],l)
                elif d==[0,-1] :
                    return func(i+u[0],j+u[1],u)
                elif d==[-1,0] :
                    return func(i+r[0],j+r[1],r)
        
        ans=func(0,0,r)
        return ans