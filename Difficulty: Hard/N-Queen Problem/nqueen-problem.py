#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        ans=[]
        col=[False]*n
        dia1=[False]*(2*n-1)
        dia2=[False]*(2*n-1)
        def dfs(i,cur):
            if i==n:
                ans.append(cur)
            else:
                for j in range(n):
                    if col[j] or dia1[i+j] or dia2[j-i+n-1]:
                        continue
                    col[j]=dia1[i+j]=dia2[j-i+n-1]=True
                    dfs(i+1,cur+[j+1])
                    col[j]=dia1[i+j]=dia2[j-i+n-1]=False
        dfs(0,[])
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends