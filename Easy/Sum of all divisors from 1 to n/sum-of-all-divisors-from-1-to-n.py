#User function Template for python3
import math

class Solution:
    def sumOfDivisors(self, n):
    	#code here 
    	s=0
    	for i in range(1,n+1) :
    	    s += (n//i)*i
    	return s
#Calculating F(i) for every I will take almost (n rootN)
#But by observation we can find for example N = 5
#F(1) = 1 
#F(2) = 1 + 2
#F(3) = 1 + 3
#F(4) = 1 + 2 + 4
#F(5) = 1 + 5
#Now counting no of occurences of every ith number
#i = 1  OCCURence : N times (5 times)
#i = 2 occurence : N/2 times (2 times)
#i = 3 occurence : N/3 times ( 1 times)
#... and so on
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
# } Driver Code Ends