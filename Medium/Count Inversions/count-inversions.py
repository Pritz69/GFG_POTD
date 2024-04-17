class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        def merge(arr,l,m,h) :
            t=[]
            c=0
            le=l
            ri=m+1
            while le<=m and ri<=h :
                if arr[le] <= arr[ri] :
                    t.append(arr[le])
                    le +=1
                else :
                    c += (m-le +1)
                    t.append(arr[ri])
                    ri +=1
            while le<=m :
                t.append(arr[le])
                le +=1
            while ri<=h :
                t.append(arr[ri])
                ri +=1
            for i in range(l,h+1) :
                arr[i]=t[i-l]
            return c
        def mergesort(arr,l,h) :
            cnt=0
            if l >= h :
                return cnt
            m=(l+h)//2
            cnt += mergesort(arr,l,m)
            cnt += mergesort(arr,m+1,h)
            cnt += merge(arr,l,m,h)
            return cnt
        return mergesort(arr,0,n-1)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends