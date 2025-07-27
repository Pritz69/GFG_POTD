class Solution:
    def setMatrixZeroes(self, mat):
        # code here
        n=len(mat)
        m=len(mat[0])
        sr=set()
        sc=set()
        for i in range(n) :
            for j in range(m) :
                if mat[i][j]==0 :
                    sr.add(i)
                    sc.add(j)
        for i in range(n) :
            for j in range(m) :
                if i in sr or j in sc :
                    mat[i][j]=0
        return mat
        