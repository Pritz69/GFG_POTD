

class Solution {
    // Function to return a list containing the DFS traversal of the graph.
    public void dfs(ArrayList<ArrayList<Integer>> adj, int vis[], ArrayList<Integer> a,int start)
    {
        a.add(start);
        vis[start]=1;
        for( int x: adj.get(start))
        {
            if(vis[x]==0)
            {
                vis[x]=1;
                dfs(adj,vis,a,x);
            }
        }
    }
    public ArrayList<Integer> dfsOfGraph(int V, ArrayList<ArrayList<Integer>> adj) {
        // Code here
        ArrayList<Integer> a=new ArrayList<Integer>();
        int vis[]=new int[V+1];
        dfs(adj,vis,a,0);
        return a;
    }
}
