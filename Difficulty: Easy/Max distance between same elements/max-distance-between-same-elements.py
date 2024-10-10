from collections import defaultdict
class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        d=defaultdict(list)
        for i,x in enumerate(arr) :
            d[x].append(i)
        c=0
        for x in d :
            c=max(c,d[x][-1]-d[x][0])
        return c


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxDistance(arr))

# } Driver Code Ends