#{ 
 # Driver Code Starts
#Initial Template for Python 3
from typing import List


# } Driver Code Ends

import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Your code here
        d={}
        i=0
        for x,y in points :
            ans=math.sqrt(x*x + y*y)
            d[i]=ans
            i +=1
        d=sorted(d.items(),key=lambda x:x[1],)
        #print(d)
        ans=[]
        for i in range(k) :
            ans.append(points[d[i][0]])
        return ans
        

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        k = int(input())
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append([x, y])
        
        solution = Solution()
        ans = solution.kClosest(points, k)
        ans.sort()
        for point in ans:
            print(point[0], point[1])
        print("~")

# } Driver Code Ends