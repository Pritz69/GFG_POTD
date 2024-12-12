class Solution:
    def countFreq(self, arr, target):
        #code here
        n=len(arr)
        lb=n
        l,h=0,n-1
        while l <= h :
            m=(l+h)//2
            if arr[m] >= target :
                lb=m
                h=m-1
            else :
                l=m+1
        ub=n
        l,h=0,n-1
        while l <= h :
            m=(l+h)//2
            if arr[m] > target :
                ub=m
                h=m-1
            else :
                l=m+1
        
        return ub-lb


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.countFreq(A, D)
        print(ans)
        print("~")

# } Driver Code Ends