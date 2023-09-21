#User function Template for python3


class Solution:
    def find(self, arr, n, x):
        
        # code here
        lb=-1
        l=0
        r=n-1
        while l<=r :
            m=(l+r)//2
            if arr[m] >=x :
                r=m-1
                if arr[m]==x :
                    lb=m
            else :
                l=m+1
        ub=-1
        l=0
        r=n-1
        while l<=r :
            m=(l+r)//2
            if arr[m] ==x :
                ub=m
            if arr[m] >x :
                r=m-1
            else :
                l=m+1
        
        return [lb,ub]





#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends