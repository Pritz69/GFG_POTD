#User function Template for python3
from collections import defaultdict 
class Solution:
    def substrCount (self,s, k):
        # your code here
        def helper(s,k) :
            i=0
            j=0
            cnt=0
            res=0
            d=defaultdict(int)
            while j < len(s) :
                temp=0
                d[s[j]] += 1
                if d[s[j]]==1 :
                    cnt +=1
                while cnt > k :
                    d[s[i]] -=1
                    if d[s[i]] == 0 :
                        cnt -=1
                    i +=1
                temp = j-i +1
                res += temp
                j +=1
            return res
            
        return helper(s,k) - helper(s,k-1)
    
# AKSHAY ANIL        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
# } Driver Code Ends