//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function template for C++

class Solution {
  public:
    int lps(string str) {
        long long pre = 0, suf = 0, base = 29, p = 1, ind = 0, n = str.size(), mod = 1e9+7;
        
        for(int i=0; i<n-1; i++){
            int cha = str[i] - 'a' + 1;
            int chp = str[n-i-1] - 'a' + 1;
            
            pre = ((pre*base)%mod + cha)%mod;
            suf = (suf + (chp*p)%mod)%mod;
      
            p=(p*base)%mod;
            if(pre == suf){
                ind = i+1;
            }
        }
        return ind;
    }
};

//{ Driver Code Starts.

int main() {

    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        string str;
        cin >> str;

        Solution ob;

        cout << ob.lps(str) << "\n";
    }

    return 0;
}

// } Driver Code Ends