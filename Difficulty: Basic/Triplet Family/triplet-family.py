class Solution:
    def findTriplet(self, arr):
        arr.sort()
        n = len(arr)
        
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if arr[i] + arr[j] == arr[k]:
                    return True
                elif arr[i] + arr[j] < arr[k]:
                    i += 1
                else:
                    j -= 1
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3
# Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.findTriplet(arr)
        if (res):
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1

# } Driver Code Ends