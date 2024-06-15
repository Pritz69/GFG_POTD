#User function Template for python3
class Solution:
	def getCount(self, n):
		# code here
		def rec(i,j,n) :
		    if i<0 or i >= 4 or j <0 or j >=3 or l[i][j] == -1:
		        return 0
		    if n==1 :
		        return 1
		    if (i,j,n) in dp :
		        return dp[(i,j,n)]
		    a=rec(i,j,n-1)
		    b=rec(i,j-1,n-1)
		    c=rec(i-1,j,n-1)
		    d=rec(i,j+1,n-1)
		    e=rec(i+1,j,n-1)
		    dp[(i,j,n)]=a+b+c+d+e
		    return dp[(i,j,n)]
		dp={}
        l=[[1,2,3],[4,5,6],[7,8,9],[-1,0,-1]]
        c=0
        for i in range(4) :
            for j in range(3) :
                if l[i][j] !=-1 :
                    c += rec(i,j,n)
        return c

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.getCount(n)
        print(ans)

# } Driver Code Ends