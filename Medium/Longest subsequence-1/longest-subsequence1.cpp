//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

class Array {
  public:
    template <class T>
    static void input(vector<T> &A, int n) {
        for (int i = 0; i < n; i++) {
            scanf("%d ", &A[i]);
        }
    }

    template <class T>
    static void print(vector<T> &A) {
        for (int i = 0; i < A.size(); i++) {
            cout << A[i] << " ";
        }
        cout << endl;
    }
};


// } Driver Code Ends

class Solution {
  public:
    int solve(int ind, vector<int> &a, int n, int prev_ind, vector<vector<int>> &dp)
    {
        if(ind == n+1)
        return 0;
        
        if(dp[ind-1][prev_ind] != -1) return dp[ind-1][prev_ind];
        
        int pick = 0;
        if(prev_ind == 0 || a[ind-1] == a[prev_ind-1]+1 || a[ind-1] == a[prev_ind-1]-1)
            pick = 1 + solve(ind+1,a,n,ind,dp);
        int nopick = 0 + solve(ind+1,a,n,prev_ind,dp);
        
        return dp[ind][prev_ind] = max(pick,nopick);
    }
    int longestSubseq(int n, vector<int> &a) {
        // code here
        vector<vector<int>> dp(n+1,vector<int>(n+1,-1));
        return solve(1,a,n,0,dp);
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    scanf("%d ", &t);
    while (t--) {

        int n;
        scanf("%d", &n);

        vector<int> a(n);
        Array::input(a, n);

        Solution obj;
        int res = obj.longestSubseq(n, a);

        cout << res << endl;
    }
}

// } Driver Code Ends