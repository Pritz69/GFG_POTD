#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        n=len(arr)
        
        for i in range(n):
            arr[i]-=1
            
        for i in range(n):
            arr[arr[i]%n]+=n
            
        for i in range(n):
            arr[i]=arr[i]//n
        
        repeating=0
        missing=0
        
        for i in range(n):
            if arr[i]==0:
                missing=i+1
            elif arr[i]>1:
                repeating=i+1
        
        return repeating,missing

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1

# } Driver Code Ends