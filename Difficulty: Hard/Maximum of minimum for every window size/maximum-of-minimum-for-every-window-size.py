def prevS(arr,n):
    stack = []
    res = [None] * n
    
    for i in range(n):
        while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
            stack.pop()
        
        if len(stack) == 0:
            res[i] = -1
        else:
            res[i] = stack[-1]
        stack.append(i)
    return res
def nextS(arr,n):
    stack = []
    res = [None] * n
    for i in range(n-1,-1,-1):
        while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if len(stack) == 0:
            res[i] = n
        else:
            res[i] = stack[-1]
        stack.append(i)
    return res
class Solution:
    
    #Function to find maximum of minimums of every window size.
    def maxOfMins(self,arr):
        # code here
        n = len(arr)
        ns = nextS(arr,n)
        ps = prevS(arr,n)
        
        
        ans = [0] * (n + 1)
        
        for i in range(n):
            index = ns[i] - ps[i] - 1
            ans[index] = max(arr[i],ans[index])
        for i in range(n - 1,-1,-1):
            ans[i] = max(ans[i],ans[i+1])
        
        return ans[1:]


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        solution = Solution()
        result = solution.maxOfMins(arr)
        print(" ".join(map(str, result)))
        print("~")
# } Driver Code Ends