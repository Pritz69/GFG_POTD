//{ Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        while (T-- > 0) {
            int n = sc.nextInt();
            int m=sc.nextInt();
            int[][] edge = new int[m][2];
            for(int i=0;i<m;i++){
                edge[i][0]=sc.nextInt();
                edge[i][1]=sc.nextInt();
            }
            int src=sc.nextInt();
            Solution obj = new Solution();
            int res[] = obj.shortestPath(edge,n,m,src);
            for(int i=0;i<n;i++){
                System.out.print(res[i]+" ");
            }
            System.out.println();
        }
    }
}

// } Driver Code Ends


class Solution {
    
    public int[] shortestPath(int[][] edges,int n,int m ,int src) {
        // Code here
        int ans[]=new int[n];
        boolean visit[]=new boolean[n];
        Arrays.fill(ans,-1);
        HashMap<Integer,ArrayList<Integer>> map=new HashMap<>();
        for(int i[]:edges){
            int u=i[0],v=i[1];
            map.computeIfAbsent(u,k->new ArrayList<>()).add(v);
            map.computeIfAbsent(v,k->new ArrayList<>()).add(u);
        }
        Queue<Integer> q=new LinkedList<>();
        q.add(src);
        visit[src]=true;
        int level=0;
        while(!q.isEmpty()){
            int size=q.size();
            for(int i=0;i<size;i++){
                int rt=q.poll();
                ans[rt]=level;
                if(map.containsKey(rt)){    
                    for(int j:map.get(rt)){
                        if(!visit[j]){
                            q.add(j);
                            visit[j]=true;
                        }
                    }
                }
            }
            level++;
        }
        return ans;
    }
}