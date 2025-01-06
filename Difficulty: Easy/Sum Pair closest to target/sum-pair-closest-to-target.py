#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        # code here
        arr.sort()
        l=0
        n=len(arr)
        r=n-1
        mi=float('inf')
        ans=[]
        while l < r :
            if abs((arr[l]+arr[r]) - target) < mi  :
                mi=abs((arr[l]+arr[r]) - target)
                ans=[arr[l],arr[r]]
            if arr[l]+arr[r] > target :
                r -=1
            elif arr[l]+arr[r] < target :
                l +=1
            else :
                return ans
        return ans
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends