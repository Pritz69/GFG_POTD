#User function Template for python3

class Solution:
    def getSingle(self, arr):
        # code here 
        return (3*(sum(set(arr))) - sum(arr))//2

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSingle(arr)
        print(ans)
        print("~")
# } Driver Code Ends