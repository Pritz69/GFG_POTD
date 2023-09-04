#User function Template for python3

class Solution:
    def fill(self, n, m, mat):
        # code here
        def transform(r,c) :
            if r<0 or r>=n or c<0 or c>=m or mat[r][c] !='O' :
                return
            mat[r][c]='t'
            transform(r,c+1)
            transform(r,c-1)
            transform(r+1,c)
            transform(r-1,c)
        
        for i in range(n) :
            for j in range(m) :
                if mat[i][j]=='O' and (i in [0,n-1] or j in [0,m-1]) :
                    transform(i,j)
        
        for i in range(n) :
            for j in range(m) :
                if mat[i][j] =='O' :
                    mat[i][j]='X'
                if mat[i][j] =='t' :
                    mat[i][j]='O'

        return mat
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends