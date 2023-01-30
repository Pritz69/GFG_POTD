
class Solution{
  public:
    vector<int>vis;

    int count=0;

    bool dfs(vector<int>adj[],int i){

        vis[i]=1;

        bool select = false;

        for(auto childs:adj[i]){

            if(!vis[childs] && !dfs(adj,childs))

            {

                select=true;

            }

        }

        if(select){

            count++;

        }

        return select;

    }

    int countVertex(int N, vector<vector<int>>edges){

        // code here

        vector<int>adj[N+1];

        vis = vector<int>(N+1,0);

        for(auto ele : edges){

            adj[ele[0]].push_back(ele[1]);

            adj[ele[1]].push_back(ele[0]);

        }

        dfs(adj,1);

        return count;

    }
};
