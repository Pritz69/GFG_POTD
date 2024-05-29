#User function Template for python3

class Solution:
    def numOfWays(self, K):
        # code here
            if K%2 == 0:
                return (K*(K-2))//4
            else:
                return ((K-1)*(K-1))//4

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        K=int(input())
        
        ob = Solution()
        print(ob.numOfWays(K))
# } Driver Code Ends