
class Pair
{
    int first,second;
    Pair(int f,int s)
    {
        first=f;
        second=s;
    }
}
//User function Template for Java

class Solution {
    public void toposort(ArrayList<ArrayList<Pair>> adj,Stack<Integer> st,int vis[],int node)
    {
        vis[node]=1;
        for(int i=0;i<adj.get(node).size();i++)
        {
            int x=adj.get(node).get(i).first;
            if (vis[x]==0)
            {
                toposort(adj,st,vis,x);
            }
        }
        st.push(node);
    }
	public int[] shortestPath(int N,int M, int[][] edges) {
		//Code here
		ArrayList<ArrayList<Pair>> adj=new ArrayList<>();
		for(int i=0;i<N;i++)
		{
		    ArrayList<Pair> temp=new ArrayList<>();
		    adj.add(temp);
		}
		for(int i=0;i<edges.length;i++)
		{
		    int u=edges[i][0];
		    int v=edges[i][1];
		    int wt=edges[i][2];
		    adj.get(u).add(new Pair(v,wt));
		}
		Stack<Integer> st =new Stack<>();
		int vis[]=new int[N];
		for(int i=0;i<N;i++)
		{
		    if (vis[i]==0)
		    {
		        toposort(adj,st,vis,i);
		    }
		}
		int dis[]=new int[N];
		Arrays.fill(dis,(int)1e9);
		dis[0]=0;
		while (!st.isEmpty())
		{
		    int n=st.peek();
		    st.pop();
		    for(int i=0;i<adj.get(n).size();i++)
		    {
		        int v=adj.get(n).get(i).first;
		        int w=adj.get(n).get(i).second;
		        if(dis[n]+w < dis[v])
		        {
		            dis[v]=dis[n]+w;
		        }
		    }
		}
		for(int i=0;i<N;i++)
		{
		    if(dis[i]==1e9)
		    {
		        dis[i]=-1;
		    }
		}
		return dis;
	}
}
