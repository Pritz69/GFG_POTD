#User function Template for python3

class Solution:
    def DivisibleByEight(self,s):
        #code here
        if int(s[-3:])%8 == 0 :
            return 1
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        print(ob.DivisibleByEight(S))
# } Driver Code Ends