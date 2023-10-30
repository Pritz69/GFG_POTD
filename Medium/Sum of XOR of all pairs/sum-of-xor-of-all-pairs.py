#User function Template for python3

class Solution:
    def sumXOR (self, arr, n) : 
        s=0
        for i in range(0,32):
            z=0
            for j in range(n):
                if(arr[j]&(1<<i))!=0:
                    z+=1
            s+=((n-z)*z*(1<<i))
        return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.sumXOR(arr, n)
    print(res)


# } Driver Code Ends