#User function Template for python3

class Solution:

    def countStr(self, n):
        # code here
        
        ans=1+2*n +(n*((n*n)-1))//2
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countStr(n))
# } Driver Code Ends