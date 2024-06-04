//{ Driver Code Starts

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends


class Solution {
  public:
    string binaryNextNumber(string s) {
        // code here.
        
        while(s[0] == '0') s = s.substr(1);
        
        int carry = 1;
        string ans = "";
        
        for(int i = s.size()-1; i >= 0; i--) {
            if (s[i] == '1') s[i] = '0';
            else {
                s[i] = '1';
                return s;
            }
            ans.push_back('0');
        }
        
        return '1'+ans;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;
        Solution ob;
        cout << ob.binaryNextNumber(s);
        cout << "\n";
    }

    return 0;
}
// } Driver Code Ends