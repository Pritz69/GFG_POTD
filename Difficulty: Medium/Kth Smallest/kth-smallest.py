#User function Template for python3
import heapq

class Solution:

    def kthSmallest(self, arr,k):
        
        l=[]
        heapq.heapify(l)
        for x in arr :
            heapq.heappush(l,(-1)*x)
            if len(l) > k :
                heapq.heappop(l)
        #print(l)
        return (-1)*l[0]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))

# } Driver Code Ends