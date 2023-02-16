class Solution{
public:

    int dfs(int i, vector<int>& arr, vector<int> &vis)
    {
        int n = arr.size();
        if(i>=n || i<0) return 1;
        if(vis[i]) return vis[i];
        vis[i] = -1;
        int x = dfs(i+arr[i], arr, vis);
        vis[i] = x;
        return vis[i];
    }

    int goodStones(int n,vector<int> &arr){
        vector<int> vis(n);
        int cnt = 0;
        for(int i = 0; i<n; ++i)
        dfs(i, arr, vis);
        
        for(int i = 0; i<n; ++i) cnt += vis[i]==1;
        return cnt;
    }  
};
