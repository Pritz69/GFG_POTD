

class Solution:
    
    #Function to return sum of upper and lower triangles of a matrix.
    def sumTriangles(self,matrix, n):
        # code here 
        su,s=0,0
        for i in range(n) :
            for j in range(i,n) :
                su += matrix[i][j]
        for i in range(n) :
            for k in range(i+1) :
                s += matrix[i][k]
        return [su,s]
