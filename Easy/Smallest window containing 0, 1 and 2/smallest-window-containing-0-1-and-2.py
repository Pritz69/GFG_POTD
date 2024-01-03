#User function Template for python3
from collections import defaultdict
class Solution:
    def smallestSubstring(self, S):
        # Code here
        i=0
        j=0
        s=defaultdict(int)
        m=float('inf')
        while j<len(S) :
            s[S[j]] +=1
            if len(s)==3 :
                m=min(m,j-i+1)
            while len(s)==3:
                s[S[i]]-=1
                if s[S[i]]==0:
                    s.pop(S[i])
                i +=1
                if len(s)==3 :
                    m=min(m,j-i+1)
            j +=1
        return -1 if m==float('inf') else m
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends