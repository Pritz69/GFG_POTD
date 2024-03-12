#User function Template for python3

class Solution:
    def mult(self, mat1, mat2, m):
        mat = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    mat[i][j] += mat1[i][k] * mat2[k][j]
                mat[i][j] %= m
        return mat
     
    def exp(self, mat, n, m):
        if n == 0:
            return [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        elif n == 1:
            return mat
        else:
            math = self.exp(mat, n//2, m)
            matf = self.mult(math, math, m)
            if n%2:
                matf = self.mult(matf, mat, m)
            return matf
            
    def genFibNum(self, a, b, c, n, m):
        if n <= 2:
            return 1%m
        else:
            return sum(self.exp([[a, b, c], [1, 0, 0], [0, 0, 1]], n-2, m)[0])%m

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b,c,n,m=map(int,input().split())
        
        ob = Solution()
        print(ob.genFibNum(a,b,c,n,m))
# } Driver Code Ends