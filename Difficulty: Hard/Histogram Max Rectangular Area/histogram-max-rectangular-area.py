#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends


class Solution:
    def getMaxArea(self,arr):
        #code here
        n = len(arr)
        left = [-1]*n
        right = [n]*n
        
        stk = []
        for i in range(n):
            while(stk and arr[stk[-1]] >= arr[i]):
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        stk = []
        for i in range(n-1, -1, -1):
            while(stk and arr[stk[-1]] >= arr[i]):
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)

        maxi = -1e9
        for i in range(n):
            v = (right[i] - left[i] - 1) * arr[i]
            maxi = max(v, maxi)
        return maxi


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.getMaxArea(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends