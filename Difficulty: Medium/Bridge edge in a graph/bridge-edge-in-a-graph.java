//{ Driver Code Starts
import java.util.*;


// } Driver Code Ends

class Solution {
    public boolean isBridge(int V, int[][] edges, int c, int d) {
        // Build adjacency list representation of the graph
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++) {
            adj.add(new ArrayList<>());
        }
        
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            adj.get(u).add(v);
            adj.get(v).add(u);
        }
        
        // Function to perform DFS and count reachable vertices
        int initialComponentCount = countComponents(V, adj);
        
        // Remove edge c-d from the graph
        adj.get(c).remove(Integer.valueOf(d));
        adj.get(d).remove(Integer.valueOf(c));
        
        int finalComponentCount = countComponents(V, adj);
        
        // Restore the edge c-d in the graph
        adj.get(c).add(d);
        adj.get(d).add(c);
        
        // Determine if edge c-d is a bridge
        return finalComponentCount > initialComponentCount;
    }
    
    // Helper function to count connected components using DFS
    private int countComponents(int V, List<List<Integer>> adj) {
        boolean[] visited = new boolean[V];
        int components = 0;
        
        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                dfs(i, adj, visited);
                components++;
            }
        }
        
        return components;
    }
    
    // DFS traversal to mark reachable vertices
    private void dfs(int node, List<List<Integer>> adj, boolean[] visited) {
        visited[node] = true;
        for (int neighbor : adj.get(node)) {
            if (!visited[neighbor]) {
                dfs(neighbor, adj, visited);
            }
        }
    }
}



//{ Driver Code Starts.

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = Integer.parseInt(sc.nextLine().trim());
        while (t-- > 0) {
            // V and E on separate lines
            int V = Integer.parseInt(sc.nextLine().trim());
            int E = Integer.parseInt(sc.nextLine().trim());

            // Using a 2D array to store edges.
            int[][] edges = new int[E][2];
            for (int i = 0; i < E; i++) {
                // Use split("\\s+") to handle one or more whitespace characters
                String[] parts = sc.nextLine().trim().split("\\s+");
                edges[i][0] = Integer.parseInt(parts[0]);
                edges[i][1] = Integer.parseInt(parts[1]);
            }

            // c and d on separate lines
            int c = Integer.parseInt(sc.nextLine().trim());
            int d = Integer.parseInt(sc.nextLine().trim());

            Solution obj = new Solution();
            boolean result = obj.isBridge(V, edges, c, d);
            System.out.println(result ? "true" : "false");
            System.out.println("~");
        }

        sc.close();
    }
}
// } Driver Code Ends