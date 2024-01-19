//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


class Array
{
public:
    template <class T>
    static void input(vector<T> &A,int n)
    {
        for (int i = 0; i < n; i++)
        {
            scanf("%d ",&A[i]);
        }
    }

    template <class T>
    static void print(vector<T> &A)
    {
        for (int i = 0; i < A.size(); i++)
        {
            cout << A[i] << " ";
        }
        cout << endl;
    }
};


// } Driver Code Ends

struct comp {
    bool operator()(const std::pair<int, int>& p1, const std::pair<int, int>& p2) const {
        if (p1.first != p2.first) return p1.first > p2.first;
        return p1.second < p2.second;
    }
};
class Solution {
  public:
    vector<vector<int>> kTop(vector<int>& a, int n, int k) {
        vector<int> v;
        multiset<pair<int, int>, comp> ms;
        map<int, int> mp;
       int i=0;
        vector<vector<int>> ans;
        while(i<n){
            if (ms.find({mp[a[i]], a[i]})!=ms.end()) ms.erase({mp[a[i]], a[i]});
            mp[a[i]]++;
            ms.insert({mp[a[i]], a[i]});
            v.clear(); int nk=k;
            for(auto val:ms) {
                if (nk<=0) break;
                if (val.second==0) break;
                v.push_back(val.second);
                nk--;
            }
            ans.push_back(v);
            i++;
        }

        return ans;
    }
};


//{ Driver Code Starts.

int main(){
    int t;
    scanf("%d ",&t);
    while(t--){
        
        int N;
        scanf("%d",&N);
        
        
        int K;
        scanf("%d",&K);
        
        
        vector<int> a(N);
        Array::input(a,N);
        
        Solution obj;
        vector<vector<int>> res = obj.kTop(a, N, K);
        
        for(auto it:res)
            Array::print(it);
        
    }
}

// } Driver Code Ends