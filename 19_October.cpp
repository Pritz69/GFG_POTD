class Solution
{
    bool *visited;
    vector<int>*adj;
    public:
    bool dfs(int src,int inPath,int v)
    {
        visited[src]=true;
        if(inPath==v)
        return true;
        for(auto it:adj[src])
        {
            if(!visited[it]&&dfs(it,inPath+1,v))
            return true;
        }
        visited[src]=false;
        return false;
    }
    bool check(int N,int M,vector<vector<int>> E)
    {
        // code here
        visited=new bool[N+1];
        adj=new vector<int>[N+1];
        for(int i=0;i<M;i++)
        {
            adj[E[i][0]].push_back(E[i][1]),adj[E[i][1]].push_back(E[i][0]);
        }
        for(int i=1;i<=N;i++)
        visited[i]=false;
        for(int i=1;i<=N;i++)
        if(dfs(i,1,N))
        return true;
        return false;
    }
};
