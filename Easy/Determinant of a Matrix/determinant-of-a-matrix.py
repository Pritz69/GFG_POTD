
#User function Template for python3

class Solution:
    
    #Function for finding determinant of matrix.
    def determinantOfMatrix(self,matrix,n):
        # code here 
        ans=0
        s=1
        if n==1 :
            return matrix[0][0]
        for i in range(n) :
            nmat=[[0]*(n-1) for j in range(n-1)]
            for r in range(1,n) :
                col=0
                for c in range(n) :
                    if c==i :
                        continue
                    nmat[r-1][col]=matrix[r][c]
                    col +=1
            ans += matrix[0][i] * self.determinantOfMatrix(nmat,n-1) * s
            s *= -1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        print(obj.determinantOfMatrix(matrix,n))
# } Driver Code Ends