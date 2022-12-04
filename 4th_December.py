#User function Template for python3

class Solution:
    def rearrange(self, S, N):
        result = ''
        if N == 1:
            result = S
        else:
            v = []
            c = []
            for i in S:
                if i in ['a','e','i','o','u']: v.append(i)
                else: c.append(i)
            
            V = len(v)
            C = len(c)
            v.sort()
            c.sort()
            
            
            if V == 0 or C == 0:
                result = -1
                
            elif  V == C or V == C+1 :
                for i in range(N):
                    result += v[i//2] if i%2 == 0 else c[i//2]
            
            elif C == V+1 :
                for i in range(N):
                    result += c[i//2] if i%2 == 0 else v[i//2]
            else:
                result = -1
        
        return result
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N = int(input().strip())
        S = input().strip()
        ob=Solution()
        ans=ob.rearrange(S, N)
        print(ans)
# } Driver Code Ends
