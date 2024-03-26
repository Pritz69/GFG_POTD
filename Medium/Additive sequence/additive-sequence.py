#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# return 1 in case of True and 0 in case of False
class Solution:
    def isAdditiveSequence(self, n):
        #code here
        def util(a1,a2,s):
            if not s:
                return True
            a=a1+a2
            astr=str(a)
            if not s.startswith(astr):
                return False
            return util(a2,a,s[len(astr):])
        l=len(n)
        for i in range(1,l):
            for j in range(i+1,l):
                a1,a2=int(n[:i]),int(n[i:j])
                if util(a1,a2,n[j:]):
                    return 1
        return 0



#{ 
 # Driver Code Starts.
        
if __name__ == "__main__":
    sol = Solution()
    t = int(input())
    for _ in range(t):
        s = input()
        print(sol.isAdditiveSequence(s))

# } Driver Code Ends