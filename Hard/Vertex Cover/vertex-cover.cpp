//{ Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++

class Solution{
    public:
        int vertexCover(int n, vector<pair<int, int>> &edges) {
            int ans=18;
            for(int bit=0;bit<(1<<n);bit++){
                int m=edges.size();
                for(auto i:edges){
                    int x=i.first,y=i.second;
                    x--,y--;
                  if((bit&(1<<x))|(bit&(1<<y)))
                     m--;
                  else break;
                }
            if(m==0) ans=min(ans,__builtin_popcount(bit));
            }
        return ans;
    }
};

//{ Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,m;
        cin>>n>>m;
        vector<pair<int,int>> edges;
        for(int i=0;i<m;i++)
        {
            int a,b;
            cin>>a>>b;
            edges.push_back({a,b});
        }
        Solution s;
        cout<<s.vertexCover(n,edges)<<endl;
    }
    return 0;
}
// } Driver Code Ends