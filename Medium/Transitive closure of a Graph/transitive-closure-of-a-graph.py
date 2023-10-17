#User function Template for python3

class Solution:
    def transitiveClosure(self, N, graph):
        # code here
        ans=[[0]*N for i in range(N)]
        
        def dfs(i,j) :
            ans[i][j]=1
            for x in range(N) :
                if x!=i and graph[j][x]==1 and ans[i][x]==0:
                    dfs(i,x)
                    
        for i in range(N) :
            dfs(i,i)
            
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        graph = []
        for i in range(0,N):
            graph.append([int(j) for j in input().split()])
        ob = Solution()
        ans = ob.transitiveClosure(N, graph)
        for i in range(N):
            for j in range(N):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends