//{ Driver Code Starts
import java.io.*;
import java.util.*;

public class GFG {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t=scanner.nextInt();
        while(t-- > 0)
        {
            int n = scanner.nextInt();
            int m = scanner.nextInt();
    
            ArrayList<ArrayList<Integer>> edges = new ArrayList<>();
            for (int i = 0; i < m; i++) {
                int u = scanner.nextInt();
                int v = scanner.nextInt();
                ArrayList<Integer> edge = new ArrayList<>();
                edge.add(u);
                edge.add(v);
                edges.add(edge);
            }
    
            Solution solution = new Solution();
            boolean result = solution.isTree(n, m, edges);
    
            if (result==true) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }
    }
}
// } Driver Code Ends


//User function Template for Java
class Solution {
    public boolean dfs(int node, List<Integer>[] adjm, boolean[] vis, int parent) 
    {
        vis[node] = true;
        for (int x : adjm[node]) 
        {
            if (!vis[x]) {
                if (dfs(x, adjm, vis, node) == false) 
                {
                    return false;
                    
                }
            } else if (x != parent)
            {
                // If the neighbor is already visited and not the immediate parent, a cycle exists
                return false;
            }
        }
        return true;
    }

    public boolean isTree(int n, int m, ArrayList<ArrayList<Integer>> edges) 
    {
        // code here
        List<Integer>[] adjm = new ArrayList[n];
        for (int i = 0; i < n; i++) 
        {
            adjm[i] = new ArrayList<Integer>();
        }
        for (int i = 0; i < m; i++) 
        {
            adjm[edges.get(i).get(0)].add(edges.get(i).get(1));
            adjm[edges.get(i).get(1)].add(edges.get(i).get(0));
        }
        boolean[] vis = new boolean[n];
        if (dfs(0, adjm, vis, -1) == false)
        {
            return false;
        }
        for (int j = 0; j < n; j++) 
        {
            if (vis[j] == false) 
            {
                return false;
            }
        }
        return true;
    }
}

