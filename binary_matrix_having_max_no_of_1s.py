class Solution:
    def findMaxRow(self, mat, N):
        # Code here
        m=-float('inf')
        row=0
        r =0
        for i in mat :
            cnt=i.count(1)
            if cnt>m :
                m=cnt
                row =r
            r +=1
        return row,m
