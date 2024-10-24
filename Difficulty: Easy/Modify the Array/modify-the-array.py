#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        narr=[]
        i=0
        n=len(arr)
        while i < n :
            if i+1<n and arr[i]==arr[i+1] and arr[i] > 0 :
                narr.append(arr[i]*2)
                i +=1
            elif arr[i] > 0 :
                narr.append(arr[i])
            i +=1
        for i in range(len(arr)-len(narr)) :
            narr.append(0)
        return narr

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        t -= 1


# } Driver Code Ends