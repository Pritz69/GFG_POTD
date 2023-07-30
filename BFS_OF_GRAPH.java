
class Solution {
    // Function to return Breadth First Traversal of given graph.
    public ArrayList<Integer> bfsOfGraph(int v, ArrayList<ArrayList<Integer>> adj) {
        // Code here
        Queue<Integer>q=new LinkedList<>();
        ArrayList<Integer> a=new ArrayList<>();
        int vis[]=new int[v+1];
        q.offer(0);
        vis[0]=1;
        while (!q.isEmpty())
        {
            int n=q.poll();
            a.add(n);
            for(int x:adj.get(n))
            {
                if (vis[x] !=1)
                {
                    q.offer(x);
                    vis[x]=1;
                }
            }
        }
        return a;
    }
}
