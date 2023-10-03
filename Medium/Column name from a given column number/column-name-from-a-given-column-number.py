#User function Template for python3

class Solution:
    def colName (self, n):
        # your code here
        s=""
        while n >0 :
            n-=1
            d=n%26
            s = chr(65+d) + s
            n //= 26
        return s

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends