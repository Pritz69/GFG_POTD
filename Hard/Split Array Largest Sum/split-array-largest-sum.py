#User function Template for python3

class Solution:
    def splitArray(self, arr, N, K):
        # code here
        def fun(tar) :
            c=1
            s=0
            for i in range(N) :
                if s+arr[i] <=tar :
                    s += arr[i]
                else :
                    c +=1
                    s =arr[i]
            return c
        
        lo=max(arr)
        hi=sum(arr)
        m=float('inf')
        while lo <= hi :
            mid = (lo+hi)//2
            if fun(mid)<=K :
                m=min(m,mid)
                hi=mid-1
            else :
                lo=mid+1
        return m
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.splitArray(arr,N,K))
# } Driver Code Ends