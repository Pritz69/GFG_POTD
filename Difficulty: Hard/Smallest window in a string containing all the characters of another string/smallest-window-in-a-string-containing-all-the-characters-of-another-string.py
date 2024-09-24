#User function Template for python3


class Solution:
    def smallestWindow(self, s, p):
        d = {}
        for i in p:
            d[i] = d.get(i,0) + 1
        dd = {}  
        req, match, n, mini, l, res = len(d), 0, len(s), float('inf'), 0, ""
        
        for i in range(n):
            if s[i] in d:
                dd[s[i]] = dd.get(s[i], 0) + 1
                if dd[s[i]] == d[s[i]]:
                    match += 1
            while match == req:
                if i - l + 1 < mini:
                    mini = i - l + 1
                    res = s[l:i+1]
                if s[l] in d:
                    dd[s[l]] -= 1
                    if dd[s[l]] < d[s[l]]:
                        match -= 1
                l += 1
        if res == "":
            return -1
        return res


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
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        print(ob.smallestWindow(s,p))
# } Driver Code Ends