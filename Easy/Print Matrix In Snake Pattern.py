class Solution:
    
    #Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix): 
       # code here 
        n=len(matrix)
        l=[]
        s=1
        for i in range(n) :
            if s==1 :
                for j in range(n) :
                    l.append(matrix[i][j])
            else :
                for j in range(n-1,-1,-1) :
                    l.append(matrix[i][j])
            s=s*(-1)
        return l
