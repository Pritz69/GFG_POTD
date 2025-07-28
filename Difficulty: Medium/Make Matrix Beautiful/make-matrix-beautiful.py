class Solution:
    def balanceSums(self, mat):
        # code here
        maxrs=0
        for x in mat :
            s=sum(x)
            maxrs=max(maxrs,s)
        maxcs=0
        for j in range(len(mat[0])) :
            cs=0
            for i in range(len(mat)) :
                cs += mat[i][j]
            maxcs=max(maxcs,cs)
        
        targets=max(maxcs,maxrs)
        
        rops=0
        for x in mat :
            rs=sum(x)
            rops += targets-rs
        
        cops=0
        for j in range(len(mat[0])) :
            cs=0
            for i in range(len(mat)) :
                cs += mat[i][j]
            cops += targets-cs
        
        return max(rops,cops)