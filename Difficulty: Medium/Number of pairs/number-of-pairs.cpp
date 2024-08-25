//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    long long countPairs(vector<int> &arr, vector<int> &brr) {
        int n = arr.size(), m = brr.size();
        vector<double> a(n), b(m);
        
        for(int i=0; i<n; i++){
            a[i] = log2(arr[i]) / arr[i];
        }
        
        for(int i=0; i<m; i++){
            b[i] = log2(brr[i]) / brr[i];
        }
        
        
        sort(a.begin(), a.end());
        sort(b.begin(), b.end());
        
        // log(x)/x > log(y)/y
        
        long long ans = 0;
        
        for(int i=0; i<m; i++){
            int ind = upper_bound(a.begin(), a.end(), b[i]) - a.begin();
            if(ind != n)
                ans +=(n - ind);
        }
        
        return ans;
        
    }
};




//{ Driver Code Starts.

int main() {
    int T;
    cin >> T;
    cin.ignore();
    while (T--) {
        vector<int> ex;
        vector<int> a, b;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int num;
        while (ss >> num)
            ex.push_back(num);
        a = ex;
        getline(cin, input);
        ss.clear();
        ss.str(input);
        int num2;
        while (ss >> num2)
            b.push_back(num2);

        Solution ob;
        cout << ob.countPairs(a, b) << endl;
    }
}
// } Driver Code Ends