#User function Template for python3

class Solution:
    def numberOfSubsequences (ob,N,A):
        # code here 
        mod = (10**9+7)
        
        ans = 0
        for i in range(N):
            if (A[i] & (A[i]-1)) == 0:
                ans = ((ans << 1)+ 1) % mod
            
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())
        A=list(map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.numberOfSubsequences(N,A))
# } Driver Code Ends