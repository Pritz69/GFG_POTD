#User function Template for python3

class Solution:
	def FindExitPoint(self, n, m, mat):
		# Code here
        ans=[-1,-1]
        d='r'
        i,j=0,0
        while i>=0 and i<n and j>=0 and j<m :
            ans[0],ans[1]=i,j
            if mat[i][j]==1 :
                mat[i][j]=0
                if d=='r' :
                    d='d'
                    i +=1
                elif d=='d' :
                    d='l'
                    j -=1
                elif d=='l' :
                    d='u'
                    i -=1
                else :
                    d='r'
                    j +=1
            else :
                if d=='r' :
                    j +=1
                elif d=='d' :
                    i +=1
                elif d=='l' :
                    j -=1
                else :
                    i -=1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.FindExitPoint(n, m, matrix)
        for _ in ans:
            print(_, end=" ")
        print()

# } Driver Code Ends