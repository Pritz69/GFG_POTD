class Solution:
    def rotateMatrix(self, k, mat):
        # code here
        n,m=len(mat),len(mat[0])
        rmat=[[0]*m for i in range(n)]
        if k%m ==0 :
            return mat
        ans=k%m
        for i in range(n) :
            c=0
            for j in range(ans,m) :
                rmat[i][c]=mat[i][j]
                c +=1
        for i in range(n) :
            c=m-ans
            for j in range(ans) :
                rmat[i][c]=mat[i][j]
                c +=1
        return rmat
            


#{ 
 # Driver Code Starts
import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().strip().split(" "))
        mat = []
        for i in range(n):
            mat.append(list(map(int, input().strip().split(" "))))
        ob = Solution()
        ans = ob.rotateMatrix(k, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end=" ")
            print()

# } Driver Code Ends