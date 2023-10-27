#User function Template for python3

class Solution:
    def minimumNumberOfDeletions(self,S):
        # code here 
        def lcs(s1,s2) :
            x=len(s1)
            y=len(s2)
            dp = [[0]*(y+1) for i in range(x+1)]
            for i in range(1,x+1) :
                for j in range(1,y+1) :
                    if s1[i-1]==s2[j-1] :
                        dp[i][j]=dp[i-1][j-1]+1
                    else :
                        dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            
            return dp[x][y]
            
        longestpalinsubseq=lcs(S,S[::-1])
        mindeletions=len(S)-longestpalinsubseq
        
        return mindeletions

# VARIANT OF LCS,LPS
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=input()

        ob = Solution()
        print(ob.minimumNumberOfDeletions(S))
# } Driver Code Ends