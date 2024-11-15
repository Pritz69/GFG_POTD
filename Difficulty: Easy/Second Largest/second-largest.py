#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        if len(arr)==1 :
            return -1
        arr.sort()
        a=arr[-1]
        for i in range(len(arr)-1,-1,-1) :
            if a!=arr[i] :
                return arr[i]
        return -1

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends