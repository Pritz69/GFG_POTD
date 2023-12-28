#User function Template for python3

class Solution:
    def match(self, wild, pattern):
        # code here
        def rec(i,j) :
            if i==len(wild) or j==len(pattern):
                if j==len(pattern) and i==len(wild):
                    return 1
                else :
                    return 0
            if (i,j) in dp :
                return dp[(i,j)]
            res=0
            if wild[i]==pattern[j] :
                res = rec(i+1,j+1)
            else :
                if wild[i]=='?' :
                    res = rec(i+1,j+1)
                elif wild[i]=='*' :
                    for k in range(j,len(pattern)+1) :
                        res += rec(i+1,k)
                else :
                    res=0
            dp[(i,j)]=res
            return res
        dp={}
        return rec(0,0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        wild = input()
        pattern = input()
        
        ob = Solution()
        if(ob.match(wild, pattern)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends