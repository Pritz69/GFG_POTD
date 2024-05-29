//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
  
    int rec(int n, int x, int y,vector<int>&dp){
        if(n == 0)
            return false;
        
        if(n == 1 )
            return true;
        
        if(dp[n] != -1)
            return dp[n];
        
        if(!rec(n-1, x, y, dp)){
            return  dp[n] = true;
        }
        if(x<=n && !rec(n-x, x, y, dp)){
            return dp[n] = true;
        }
        if(y<=n && !rec(n-y, x, y, dp)){
            return dp[n] = true;
        }
        
        return dp[n] = false;
    }
  
    int findWinner(int n, int x, int y) {
        vector<int>dp(n+1,-1);
        return rec(n, x, y, dp);
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    scanf("%d ", &t);
    while (t--) {

        int n;
        scanf("%d", &n);

        int x;
        scanf("%d", &x);

        int y;
        scanf("%d", &y);

        Solution obj;
        int res = obj.findWinner(n, x, y);

        cout << res << endl;
    }
}

// } Driver Code Ends