class Solution:
    def maxLen(self, arr):
        # code here

        m,s,ml={},0,0
        for i in range(len(arr)):
            s+=(1 if arr[i]==1 else -1)
            if s==0: 
                ml=i+1
            elif s in m: 
                ml=max(ml,i-m[s])
            else: 
                m[s]=i
        return ml
#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends