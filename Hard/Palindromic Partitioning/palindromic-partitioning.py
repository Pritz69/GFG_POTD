#User function Template for python3

class Solution:
    def palindromicPartition(self, string):
        # code here
        def ispalin(i,j,s) :
            while i<=j :
                if s[i] != s[j] :
                    return False
                i +=1
                j -=1
            return True
        def rec(i) :
            if i==len(string) :
                return 0
            if i in dp :
                return dp[i]
            mi=float('inf')
            for j in range(i,len(string)) :
                if ispalin(i,j,string) :
                    mi = min(mi,1 + rec(j+1))
            dp[i]=mi
            return dp[i]
        dp={}
        return rec(0)-1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends