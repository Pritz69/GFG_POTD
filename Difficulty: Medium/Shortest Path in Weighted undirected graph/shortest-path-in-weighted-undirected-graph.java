//{ Driver Code Starts
import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br;
    static PrintWriter ot;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        ot = new PrintWriter(System.out);

        int t = Integer.parseInt(br.readLine().trim());

        while (t-- > 0) {
            String s[] = br.readLine().trim().split(" ");
            int n = Integer.parseInt(s[0]), m = Integer.parseInt(s[1]);
            int edges[][] = new int[m][3];
            for (int i = 0; i < m; i++) {
                s = br.readLine().trim().split(" ");
                edges[i][0] = Integer.parseInt(s[0]);
                edges[i][1] = Integer.parseInt(s[1]);
                edges[i][2] = Integer.parseInt(s[2]);
            }

            List<Integer> list = new Solution().shortestPath(n, m, edges);

            ot.println(list.get(0));
            if (list.get(0) != -1 && !check(list, edges)) ot.println(-1);
        }
        ot.close();
    }

    static boolean check(List<Integer> list, int edges[][]) {
        Set<Integer> hs = new HashSet<>();
        Map<Integer, Map<Integer, Integer>> hm = new HashMap<>();
        for (int i = 1; i < list.size(); i++) hs.add(list.get(i));
        for (int x[] : edges) {
            if (hs.contains(x[0]) || hs.contains(x[1])) {
                if (!hm.containsKey(x[0])) hm.put(x[0], new HashMap<>());
                if (!hm.containsKey(x[1])) hm.put(x[1], new HashMap<>());
                hm.get(x[0]).put(x[1], x[2]);
                hm.get(x[1]).put(x[0], x[2]);
            }
        }
        int sum = 0;
        for (int i = 1; i < list.size() - 1; i++) {
            if (!hm.containsKey(list.get(i)) ||
                !hm.get(list.get(i)).containsKey(list.get(i + 1)))
                return false;
            sum += hm.get(list.get(i)).get(list.get(i + 1));
        }
        return sum == list.get(0);
    }
}

// } Driver Code Ends

class Solution {
    public List<Integer> shortestPath(int n, int m, int edges[][]) {
        //  Code Here.
        //Initialization of adjacencylist 
        List<List<int[]>> adj=new ArrayList<>();
        for(int i=0;i<=n;i++) adj.add(new ArrayList<>());
        for(int[] e:edges){
            adj.get(e[0]).add(new int[]{e[1],e[2]});
            adj.get(e[1]).add(new int[]{e[0],e[2]});
        }
        //Iitialization of distances as max and parents
        int dis[]=new int[n+1],parent[]=new int[n+1];
        Arrays.fill(dis,(int)(1e9));
        Queue<int[]> pq=new PriorityQueue<>((x,y)->x[1]-y[1]); //sort based on distances
        pq.add(new int[]{1,0});
        dis[1]=0;
        //traversal and finding the minimum distances
        while(!pq.isEmpty()){
            int[] curr=pq.poll();
            int u=curr[0],d=curr[1]; //u->current node, d->distance from 1
            if(d>dis[u]) continue;
            for(int[] a:adj.get(u)){
                int v=a[0],w=a[1]; //v->node connected to u, w->distance from u to v
                if(dis[u]+w<dis[v]){
                    dis[v]=dis[u]+w;
                    parent[v]=u;
                    pq.add(new int[]{v,dis[v]});
                }
            }
        }
        //If from 1-n not possible 
        if(dis[n]==(int)(1e9)) return Arrays.asList(-1);
        //find the shortest path from n to 1 and then reverse it
        List<Integer> ans=new ArrayList<>();
        int node=n;
        while(node!=0){
            ans.add(node);
            node=parent[node];
        }
        ans.add(dis[n]);
        Collections.reverse(ans);
        return ans;
    }
}