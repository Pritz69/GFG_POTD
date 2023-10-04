#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        # code here
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans=0
        i=0
        while i < len(S) :
            if i+1 <len(S) and d[S[i+1]] > d[S[i]] :
                ans +=d[S[i+1]]-d[S[i]]
                i +=2
            else :
                ans += d[S[i]]
                i +=1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends