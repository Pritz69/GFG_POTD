#User function Template for python3
class Solution:
	def countPairsWithDiffK(self,arr, k):
    	# code here
        d={}
        for x in arr :
            d[x]=d.get(x,0)+1
        visited = set()
        c = 0
        
        # Iterate through each unique element
        for x in d:
            if k == 0:
                # Special case: count pairs (x, x) if k = 0
                c += d[x] * (d[x] - 1) // 2
            elif (x + k) in d:
                # Count pairs (x, x + k) if k != 0
                c += d[x] * d[x + k]
        
        return c



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.countPairsWithDiffK(arr, k)
        print(ans)
        print("~")
        tc -= 1

# } Driver Code Ends