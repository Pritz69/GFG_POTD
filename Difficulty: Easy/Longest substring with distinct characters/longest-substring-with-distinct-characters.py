#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        count=[-1]*26
        n=len(s)
        preIndx=-1
        ans=0
        for i in range(n):
            pos=ord(s[i])-ord("a")
            if count[pos]!=-1:
                preIndx=max(preIndx,count[pos])
            count[pos]=i
            ans=max(ans,i-preIndx)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends