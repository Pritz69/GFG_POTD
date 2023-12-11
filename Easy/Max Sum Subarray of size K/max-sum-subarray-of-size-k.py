#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        l=0
        r=0
        ma=float('-inf')
        s=0
        while r<N :
            s+=Arr[r]
            if r-l+1 == K :
               ma=max(s,ma)
               s-=Arr[l]
               l +=1
            r +=1
        return ma


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends