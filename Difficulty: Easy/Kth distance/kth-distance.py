#User function Template for python3
from collections import defaultdict
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # your code
        d=defaultdict(list)
        for i,x in enumerate(arr) :
            d[x].append(i)
        for x in d :
            for i in range(len(d[x])-1) :
                if d[x][i+1]-d[x][i] <= k :
                    return True
        return False
#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.checkDuplicatesWithinK(arr, k)
        if res:
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1
# } Driver Code Ends