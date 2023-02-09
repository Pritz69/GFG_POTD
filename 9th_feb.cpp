class Solution {
public:
vector<int> vis;
vector<int> matching;
    bool solve(int person, vector<vector<int>>&G){       
        for(int job=0;job<G[0].size();job++){     
            //check if the person is intrested in job
            // and the job is not occupied by anyone
            // visit that
            if(G[person][job]==1 and !vis[job]){
                vis[job]=1;                
                // if the matching is vacant means no one is assigned to it
                // or the person who is assigned can be replace to some other job 
                if(matching[job]==-1 or solve(matching[job],G)){                    
                    matching[job]=person;
                    return true;
                }
            }      
        }
        return false;    
    }
int maximumMatch(vector<vector<int>>&G){
    int n = G[0].size(), m=G.size();
    int ans=0; 
    matching=vector<int>(n,-1);
    // iterating over the persons
    for(int i=0;i<m;i++){
        //vis jobs
        vis=vector<int>(n,0);
        if(solve(i,G))
            ans++;
    }
    return ans;
}
};
