
class Solution:
    def countDistinct(self, arr, k):
        # Code here
        d={}
        ans=[]
        l=0
        for i in range(len(arr)) :
            e=arr[i]
            d[e]=d.get(e,0)+1
            if (i-l)+1==k :
                ans.append(len(d))
                le=arr[l]
                d[le] -=1
                if d[le]==0 :
                    d.pop(le)
                l +=1
        return ans

#{ 
 # Driver Code Starts
import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

# } Driver Code Ends