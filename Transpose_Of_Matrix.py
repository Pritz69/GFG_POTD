class Solution:
    def transpose(self, matrix, n):
        # Write Your code here
        for i in range(n) :
            for j in range(i+1,n) :
                t=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=t
        return matrix
