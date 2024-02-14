//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while(T-->0)
        {
            String[] s = br.readLine().trim().split(" ");
            int V = Integer.parseInt(s[0]);
            int E = Integer.parseInt(s[1]);
            ArrayList<ArrayList<Integer>>adj = new ArrayList<>();
            for(int i = 0; i < V; i++)
                adj.add(i, new ArrayList<Integer>());
            for(int i = 0; i < E; i++){
                String[] S = br.readLine().trim().split(" ");
                int u = Integer.parseInt(S[0]);
                int v = Integer.parseInt(S[1]);
                adj.get(u).add(v);
                adj.get(v).add(u);
            }
            Solution obj = new Solution();
            ArrayList<ArrayList<Integer>> ans = obj.criticalConnections(V, adj);
            for(int i=0;i<ans.size();i++)
                System.out.println(ans.get(i).get(0) + " " + ans.get(i).get(1));
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution
{
    public ArrayList<ArrayList<Integer>> criticalConnections(int v, ArrayList<ArrayList<Integer>> adj)
    {
        boolean visited[] = new boolean[v];
		int parent = -1;
		int disc[] = new int[v];
		int low[] = new int[v];
		
		int timer = 0;
		Arrays.fill(disc, -1);
		Arrays.fill(low, -1);
		
		ArrayList<ArrayList<Integer>> ans = new ArrayList<>();
		
		for(int i=0;i<v;i++) {
			if(!visited[i]) {
				dfs(i,parent,timer,disc,low,ans,visited,adj);
			}
		}
		
		//sort 
		for(ArrayList<Integer> a : ans){
		    Collections.sort(a);
		}
		Collections.sort(ans,new Comparator<ArrayList<Integer>>() {
			@Override
			public int compare(ArrayList<Integer> a,ArrayList<Integer> b) {
				if((a.get(0)-b.get(0))==0){
				    return a.get(1)-b.get(1);
				}
				return a.get(0)-b.get(0);
			}
		});
		
		return ans;
    }
    private static void dfs(int node, int parent, int timer, int[] disc, int[] low, ArrayList<ArrayList<Integer>> ans,
			boolean[] visited, ArrayList<ArrayList<Integer>> list) {
		
		visited[node] = true;
		disc[node] = timer;
		low[node] = timer;
		timer++;
		for(Integer val : list.get(node)) {
			if(val == parent) {
				continue;
			}
			if(!visited[val]) {
				dfs(val, node, timer, disc, low, ans, visited, list);
				low[node] = Math.min(low[node],low[val]);
				if(low[val]>disc[node]) {
					ArrayList<Integer> a = new ArrayList<>();

					a.add(node);
					a.add(val);
					ans.add(a);
				}
			}else {

				low[node] = Math.min(low[node], disc[val]);
			}
		}
		
	}
    
}
    
    
    