#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        t = [1 if i > k else -1 for i in arr]
        n = len(t)
        m = 0
        p = 0
        a = {}
        
        for i in range(n):
            p = p + t[i]
            
            if p > 0:
                m = i + 1
                
            else:
                if (p-1) in a:
                    m = max(m,i-a[p-1])
                    
                if p not in a:
                    a[p] = i
                    
        return m


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        
        arr = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        print("~")
        t -= 1
# } Driver Code Ends