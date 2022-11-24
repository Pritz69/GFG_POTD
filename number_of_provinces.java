class Solution {

    static int numProvinces(ArrayList<ArrayList<Integer>> adj, int V) {

        // code here

        boolean[] vis = new boolean[V];

        int c = 0;

        for(int i = 0; i < V; i++){

            if(!vis[i]){

                c++;

                dfs(adj, i, vis);

            }

        }

        

        return c;

        

    }

    

    static void dfs(ArrayList<ArrayList<Integer>> adj, int start, boolean[] vis){

        vis[start] = true;

        for(int j = 0; j < adj.get(start).size(); j++){

            if(adj.get(start).get(j) == 1 && vis[j] == false){

                dfs(adj, j, vis);

            }

        }

        // for(int i : adj.get(start)){

        //     if(!vis[i]){

        //         dfs(adj, i, vis);

        //     }

        // }

    }

};
