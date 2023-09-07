#User function Template for python3

from typing import List
from collections import deque
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        q=deque()
        d=[float('inf')]*(100000)
        mod=100000
        d[start]=0
        q.append([start,0])
        while q :
            l=q.popleft()
            val=l[0]
            step=l[1]
            if val==end :
                return step
            for x in arr :
                nval=(val*x)%mod
                if step+1 < d[nval] :
                    d[nval] = step +1
                    if nval==end :
                        return step +1
                    q.append([nval,step+1])
        return -1
                

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends