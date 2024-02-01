#User function Template for python3
from collections import defaultdict
class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        #code here
        ch="abcdefghijklmnopqrstuvwxyz"
        cH="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        d={}
        d2={}
        for x in s :
            if x in ch :
                d[x]=d.get(x,0)+1
            elif x in cH :
                d2[x]=d2.get(x,0)+1
        #print(d)
        #print(d2)
        f=0
        for x in ch :
            if x not in d and chr(ord(x)-32) not in d2:
                    f=1
        return f==0
                
        
        
        
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
        obj = Solution()
        if(obj.checkPangram(s)):
            print(1)
        else:
            print(0)
# } Driver Code Ends