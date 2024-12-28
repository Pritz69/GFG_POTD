#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
from collections import defaultdict
class Solution:
    def findTriplets(self, arr):
        # Your code here
        if len(arr)< 3:
            return []
        if len(arr) == 3 and sum(arr) == 0:
            return [[0,1,2]]
            
        n = len(arr)
        res = []
        d = defaultdict(list)
        for i in range(n):
            d[arr[i]].append(i)
            
        for i in range(n-2):
            for j in range(i+1,n-1):
                temp = arr[i] + arr[j]
                if -temp in d:
                    for x in d[-temp]:
                        if x > j:
                            res.append([i,j,x])
        return res

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        ob = Solution()
        res = ob.findTriplets(A)
        res = sorted(res)
        if len(res) == 0:
            print('[]')
        for i in range(len(res)):
            for j in range(len(res[i])):
                print(res[i][j], end=" ")
            print("")
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends