#User function Template for python3
class Solution:

	def countStrings(self,n):
    	# code here
        a,b=1,1
        c=0
        for i in range(n):
            c=(a+b)%(10**9 +7)
            a=b
            b=c
        return c
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.countStrings( n)
        print(ans)
        tc=tc-1
# } Driver Code Ends