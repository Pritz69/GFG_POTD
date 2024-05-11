#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def bitManipulation(self, n, i):
        # Code here
        getbit = 1 if n & (1<<(i-1)) else 0
        setbit = n |(1<<(i-1))
        clearbit = n & ~(1<<(i-1))
        print(getbit,setbit,clearbit,end = "")

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n, i = list(map(int, input().split()))
        ob = Solution()
        ob.bitManipulation(n, i)
        print()
# } Driver Code Ends