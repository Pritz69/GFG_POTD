#User function Template for python3

class Solution:
    def printClosest (self,arr, brr, n, m, x) : 
        #code here
        i,j=0,m-1
        diff=float("inf")
        ans=None
        while i<n and j>=0:
            sum=arr[i]+brr[j]
            if abs(sum-x)<diff:
                diff=abs(sum-x)
                ans=(arr[i],brr[j])
            if sum>x :
                j-=1
            else :
                i+=1
        return ans    
#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().strip().split()))
    brr = list(map(int, input().strip().split()))
    x = int(input())
    ob = Solution()
    ans = ob.printClosest(arr, brr, n, m, x)
    print(abs(ans[0]+ans[1] - x))
# } Driver Code Ends