def isF(arr,k,mid,n):
    count = 1
    m_sum = 0
    for i in range(n):
        
        if m_sum + arr[i] > mid:
            count += 1
            m_sum = arr[i]
        else:
            m_sum += arr[i]
    return count <= k        

class Solution:
    
    def findPages(self,arr, k):
        n = len(arr)
        if k > n:
            return -1
        high = sum(arr)
        low = max(arr)
        
        while low <= high:
            mid = (low+high)//2
            
            if isF(arr,k,mid,n):
                high = mid - 1
                res = mid
            else:
                low = mid + 1
        return res



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
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends